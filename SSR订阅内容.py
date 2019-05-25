import os
import base64

import requests

root_dir = os.path.dirname(__file__)
res = requests.get("https://raw.githubusercontent.com/AmazingDM/sub/master/ssrshare.com")

print(res)
ssr_info = base64.b64decode(res.text)

with open(os.path.join(root_dir, "SSR订阅内容.txt"), "wb") as file:
    file.write(ssr_info)
