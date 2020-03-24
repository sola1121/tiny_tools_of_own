import os


command = "pip3 list"

reback = os.popen(command)
print(reback.read())
