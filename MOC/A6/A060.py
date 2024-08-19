
import string
import time

text = 'Hello World'
temp = ''

for ch in text:
    for i in string.printable:
        if i == ch:
            time.sleep(0.01)
            print(temp+i)
            temp += ch
            break
        else:
            time.sleep(0.01)
            print(temp+i)
