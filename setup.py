"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['battery_app.py']
DATA_FILES = ["Assets/battery_charging_icon.png", "Assets/battery_charging_1.png", "Assets/battery_charging_2.png",
              "Assets/battery_charging_3.png", "Assets/battery_charging_4.png", "Assets/battery_charging_5.png"]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'Assets/icon.icns',
    'plist': {
        'LSUIElement': True
    }
}

setup(
    app=APP,
    name="Battery App",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
