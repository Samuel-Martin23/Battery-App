# -*- mode: python ; coding: utf-8 -*-

block_cipher = None



a = Analysis(['/Users/samuelmartin/Desktop/Stuff/Battery App/battery_app.py'],
             pathex=['/Users/samuelmartin/Desktop/Stuff/Battery App'],
             binaries=[('/System/Library/Frameworks/Tk.framework/Tk', 'tk'), ('/System/Library/Frameworks/Tcl.framework/Tcl', 'tcl')],
             datas=[("/Users/samuelmartin/Desktop/Stuff/Battery App/Assets/*.png", "/Users/samuelmartin/Desktop/Battery App.app/")],
             hiddenimports=['psutil'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Battery App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )