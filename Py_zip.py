import re
import os
import zipfile


regex = re.compile(r"^\d{2,4}-\d{0,2}[\s\S]*")   # TODO: 在这里自定义匹配的文件名
root_dir = os.path.dirname(__file__)

with zipfile.ZipFile(os.path.join(root_dir, "新建压缩.zip"), 'w') as new_zip:
    filenames = os.listdir(root_dir)
    for filename in filenames:
        if  regex.match(filename):
            new_zip.write(os.path.join(root_dir, filename), "文件/%s"%filename)
    else:
        print("已压缩文件\n", "\n".join(new_zip.namelist()), sep="")

print("当前zip归档已保存在同目录下\n")
