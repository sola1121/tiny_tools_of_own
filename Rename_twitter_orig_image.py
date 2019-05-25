import os
import re


count = 0
new_name_lst = list()

name_parttern = re.compile(r"([\s\S]*)_orig$")

pwd = os.path.dirname(__file__)
dir_list = os.listdir(pwd)


for filename in dir_list:
    if os.path.isfile(pwd+"/"+str(filename)):
        result = name_parttern.search(filename)
        if result:
            new_name = result.group(1)
            for i in range(1, 100):
                if (new_name in dir_list) or (new_name in new_name_lst):
                    prefix_name, suffix_name = new_name.split(".")
                    prefix_name += "({})".format(i)
                    new_name = prefix_name + "." + suffix_name
                else:
                    break
            new_name_lst.append(new_name)

            print(filename, "-->", new_name)
            os.rename(filename, new_name)
            count += 1

print("完成", count)
