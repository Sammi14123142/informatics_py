import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    uh = urllib.request.urlopen(address)
    data = uh.read()
    print('Retrieved',len(data),'characters')
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    s=0
    for count in counts:
        res = count.text
        res = int(res)
        s+=res
    print(s)
