import hashlib


path = ""

md5 = hashlib.md5()

try: 
    with open(path, 'rb') as file:
        md5.update(file.read())
    print("file path: %s\nmd5: %s" %( path, md5.hexdigest()) )

except Exception as ex:
    print("处理出错", str(ex))