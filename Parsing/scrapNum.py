from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
s=0
for tag in tags:
    num=tag.contents[0]
    n = int(num)
    s+=n
print(s)
