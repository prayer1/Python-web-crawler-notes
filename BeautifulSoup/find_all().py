import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
temo = r.text
soup = BeautifulSoup(temo, "html.parser")
print(soup.find_all('a'))
print(soup.find_all(['a', 'b']))
for tag in soup.find_all(True):
    print(tag.name)

import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)