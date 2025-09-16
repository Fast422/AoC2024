import re
with open("input1.txt", "r") as f:
    s = f.read()

print(s)

pattern = re.compile(r"mul\((\d+),(\d+)\)")

res = 0

for match in pattern.finditer(s):
    print(f"{match.group(1)} {match.group(2)}")
    res += int(match.group(1)) * int(match.group(2))
print(res)

#TC: O(n)
#SC: O(n)