import os
os.chdir("C:\\Users\Library\Downloads\code")

import re
hand=open('regex_sum_42.txt')
n=0
for line in hand:
    line=line.rstrip()
    numbers=re.findall('[0-9]+',line)
    for num in numbers:
        if len(num)>0:
            n = int(num)
            n+=n
    print(n)
