import hashlib, sys, os


md5 = hashlib.md5()
sha256 = hashlib.sha256()
switch = 0

try:
    from PyQt5.QtWidgets import QApplication, QFileDialog
except:
    switch = 1


if switch == 0:

    if sys.platform == "win32":
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        desktop = winreg.QueryValueEx(key, "Desktop")[0]
    elif sys.platform == "linux":
        import getpass
        uname = getpass.getuser()
        desktop = "/home/" + uname + "/桌面"
        if not os.path.exists(desktop):
            desktop = "/home/" + uname + "/Desktop"
    else:
        desktop = "/"

    app = QApplication(sys.argv)
    file_path, button_type = QFileDialog.getOpenFileName(parent=None, caption="文件", directory=desktop, filter="*(*.*)")
    if file_path and button_type:
        try:
            with open(file_path, 'rb') as file:
                md5.update(file.read())
                sha256.update(file.read())
            print("file path: %s\n" % file_path)
            print("md5: %s\n" % md5.hexdigest())
            print("sha256: %s\n" % sha256.hexdigest())
        except Exception as ex:
            print("处理错误", str(ex))

else:
    path = ""   # 在这里手动输入路径

    try: 
        with open(path, 'rb') as file:
            md5.update(file.read())
            sha256.update(file.read())
            print("file path: %s\n" % file_path)
            print("md5: %s\n" % md5.hexdigest())
            print("sha256: %s\n" % sha256.hexdigest())

    except Exception as ex:
        print("处理出错", str(ex))