import os
import time
import random
import requests

head = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"}

_file_name = list()

def random_name(num):
    """随机生成num个字符"""
    global _file_name
    result = ""
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(num):
        result += random.choice(seed)
    while True:
        if result in _file_name:
            result += random.choice(seed)
        else:
            _file_name.append(result)
            return result

def get_valid_name(name):
    """排除系统不可用字符小工具"""
    name = str(name)
    for invalid_str in ("/", "\\", ":", "*", "\"", "<", ">", "|", "?"):
        name = str(name).replace(invalid_str, " ")
    return str(name).strip()

def link_to(link):
    """连接网址,返回连接内容,错误尝试三次"""
    count = 1
    while True:
        try:
            res = requests.get(link, headers=head)
            if res.status_code != 200:
                raise Exception("连接地址失败.")
            return res
        except Exception as e:
            print(e)
            if count > 3:
                break
            count += 1
            time.sleep(random.randint(2, 5))

def save_image(image_link, directory, file_name):
    res = link_to(image_link)
    if not os.path.exists(directory):
        os.makedirs(directory)
    whole_name = directory + "\\" + file_name
    with open(whole_name, 'wb') as im_file:
        im_file.write(res.content)

