import hashlib, sys, os


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

    md5 = hashlib.md5()

    app = QApplication(sys.argv)
    file_path, button_type = QFileDialog.getOpenFileName(parent=None, caption="文件", directory=desktop, filter="*(*.*)")
    if file_path and button_type:
        try:
            with open(file_path, 'rb') as file:
                md5.update(file.read())
            print("file path: %s\nmd5: %s" %( file_path, md5.hexdigest()) )
        except Exception as ex:
            print("处理错误", str(ex))

else:
    path = ""

    md5 = hashlib.md5()

    try: 
        with open(path, 'rb') as file:
            md5.update(file.read())
        print("file path: %s\nmd5: %s" %( path, md5.hexdigest()) )

    except Exception as ex:
        print("处理出错", str(ex))