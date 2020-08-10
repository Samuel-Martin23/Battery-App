import sys
import psutil
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QSystemTrayIcon, QMenu, QAction, QApplication)
from threading import Timer
from os import system, path, popen


def get_path_to_resources():
    paths = popen("mdfind -name Battery App").readlines()
    for p in paths:
        if p[-5:] == ".app\n":
            return p.replace("\n", "") + "/Contents/Resources/"


def send_battery_level_notification(battery_level, battery_image):
    path_to_script = resource_path("send_battery_notification.scpt").replace(" ", "\\ ")
    message_notification = "Current battery level: {}%".format(battery_level)
    image_path = battery_image[1:].replace("/", ":", battery_image.count("/"))

    system('osascript {} "{}" "{}"'.format(path_to_script, message_notification, image_path))


def check_battery():
    if popen("ioreg -r -k AppleClamshellState -d 4 | grep AppleClamshellState  | head -1").\
               readline()[-4:].strip() == "No":
        global thread
        global check_plugged
        global previous_percent
        current_percent = psutil.sensors_battery().percent
        plugged = psutil.sensors_battery().power_plugged

        if plugged and check_plugged:
            previous_percent = 0
            check_plugged = False
        elif not plugged and not check_plugged:
            previous_percent = 0
            check_plugged = True

        for i in range(0, len(battery_levels_numbers)):
            if current_percent == battery_levels_numbers[i] and previous_percent != battery_levels_numbers[i]:
                send_battery_level_notification(battery_levels_numbers[i], resource_path(battery_levels_images[i]))
                previous_percent = current_percent

    thread = Timer(5, check_battery)
    thread.start()


def close_app():
    app.quit()
    thread.cancel()


def resource_path(relative_path):
    return path.join(path_to_resources, relative_path)


def run():
    """
    System tray code from LearnPyQt
    https://www.learnpyqt.com/courses/adanced-ui-features/system-tray-mac-menu-bar-applications-pyqt/
    """
    app.setQuitOnLastWindowClosed(False)
    # Create the icon
    image_path = resource_path("battery_charging_icon.png")
    icon = QIcon(image_path)

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()

    # Add a Quit option to the menu.
    quit_app = QAction("Quit")
    quit_app.triggered.connect(close_app)
    menu.addAction(quit_app)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    sys.exit(app.exec_())


battery_levels_numbers = [100, 80, 60, 40, 20]
battery_levels_images = ["battery_charging_1.png", "battery_charging_2.png",
                         "battery_charging_3.png", "battery_charging_4.png", "battery_charging_5.png"]
thread = None
check_plugged = True
previous_percent = 0
path_to_resources = get_path_to_resources()
app = QApplication([])
check_battery()
run()
