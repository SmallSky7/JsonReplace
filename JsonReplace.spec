# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['JsonReplace.py'],
             pathex=['JsonReplace_MainFunction.py', 'Function', 'F:\\Python Project\\JsonReplace'],
             binaries=[],
             datas=[],
             hiddenimports=['Function.Date_ReplaceController', 'Function.initdate_ReplaceController', 'Function.Modify_suffix', 'Function.Position_strController', 'Function.Symbol_ReplaceController', 'Function.Symbol_ReplaceFunction'],
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
          name='JsonReplace',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon_128px.ico')
