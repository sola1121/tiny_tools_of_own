#!/usr/bin/python3
import os
import requests


# 预先配置
count = 0
file_name_count = 0
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.130 Chrome/79.0.3945.130 Safari/537.36"
}
native_proxies = {
    "http": "127.0.0.1:1080",
    "https": "127.0.0.1:1080",
}

print("建立进程PID - ", os.getpid())
to_download_url = input("输入下载连接: ")
file_name = to_download_url.split("/")[-1]
full_path= str()

while os.path.isfile(os.path.join(os.path.dirname(__file__), file_name)):
    file_name_count += 1
    file_name = '{}_{}'.format(file_name_count, file_name)
else:
    full_path = os.path.join(os.path.dirname(__file__), file_name)
    print("写入 ", full_path)

try:
    res_file = requests.get(url=to_download_url, headers=headers, stream=True, proxies=native_proxies, timeout=30)
    print(res_file.headers)
    if res_file.status_code == 200:
        with open(full_path + ".downloading", 'wb') as chunk_file:
            for chunk in res_file.iter_content(chunk_size=128):
                count += 1
                print("\rGet chunk", count*128/1024, end='')
                chunk_file.write(chunk)
        os.rename(full_path + ".downloading", full_path)
    else:
        print("请求没有成功.\n")
except Exception as Ex:
    print('\n', Ex, sep='')
print('\n')
