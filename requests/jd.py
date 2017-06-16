import requests
url = "https://item.jd.com/4294930.html"
def getHTMLTEXT(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        return "爬取失败"
getHTMLTEXT(url)