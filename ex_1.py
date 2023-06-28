import re

f = open("data.txt", "r")

str = f.read()

datas = str.split("\n")

values = []

for d in datas:
    try :
        i = int(d)
        values.append(i)
    except:
        pass

sum = 0
for v in values:
    sum += v
    print(v)

print(sum)