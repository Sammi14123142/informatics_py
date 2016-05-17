from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - URL')
count = input('Enter - count')
count = int(count)
pos = input('Enter - position')
pos = int(pos)

i = 0
while i<count:
    
    html = urlopen(url).read()

    soup = BeautifulSoup(html)

    tags = soup('a')
    tag = tags[pos-1]
    url = tag.get('href',None)
    print(url)
    i+=1
    
