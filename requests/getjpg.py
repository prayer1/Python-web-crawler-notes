import requests
import os
root = "F://images//"
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path, "wb") as f:
            f.write(r.content)
            print("爬取成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")