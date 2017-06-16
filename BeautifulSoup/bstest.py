import requests
from bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
print(r.status_code)
r.encoding = r.apparent_encoding
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())