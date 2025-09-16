import re
with open("input1.txt", "r") as f:
    s = f.read()

print(s)

pattern = re.compile(r"mul\((\d+),(\d+)\)|(do|don't)\(\)")

tokens = pattern.findall(s)
#print(tokens)
res = 0
do = True
for i in range(len(tokens)):
    x, y, op = tokens[i]
    if op == "don't":
        do = False
    if op == "do":
        do = True
    elif x and y and do:
        res += int(x) * int(y)

print(res)

#TC: O(n)
#SC: O(n)