import re

f = open("0607/catalog.json", "r")

str = f.read()

list = re.findall("\{([^\{^\}]+)\}", str)

ll = []

for i in range(len(list)):
    ll.append(re.findall(": \"(\w+)\"[^:]+: (\d+)", list[i]))

num = 0
minV = None
maxV = None

for litem in ll:
    if litem[0][0] == "jacket":
        num += 1
        if minV is None:
            minV = int(litem[0][1])
        elif int(litem[0][1]) < minV:
            minV = int(litem[0][1])
        if maxV is None:
            maxV = int(litem[0][1])
        elif int(litem[0][1]) > maxV:
            maxV = int(litem[0][1])

print(f"num:{num}\nmin:{minV}\nmax:{maxV}")

f.close()