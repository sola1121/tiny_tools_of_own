import os
import sys

pwd = sys.path[0] + "\\"
files = os.listdir(pwd)

drop_list = list()

for name in files:
    for i in range(1, 11):
        repeat_signal = "(" + str(i) + ")"
        if repeat_signal in name:
            drop_list.append(name)

print("找到重复标志", len(drop_list))

while True:
    comfire = input("是否要删除(Y/N): ")
    if comfire.upper() == "Y":
        count = 0
        for name in drop_list:
            os.remove(pwd + name)
            count += 1
        else:
            print(count, "删除")
            break
    elif comfire.upper() == "N":
        break
        sys.exit("退出程序")
    else:
        print("给个准话.")
