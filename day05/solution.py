from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

separator_idx = lines.index("")
instructions = lines[:separator_idx]
pages = [list(map(int, line.split(","))) for line in lines[separator_idx+1:]]

# print(instructions)
# print(pages)
tracker = defaultdict(list)

for instruction in instructions:
    before, after = map(int, instruction.split("|"))
    tracker[after].append(before)

print(tracker)

res = []


for page in pages:
    seen = set()  
    pages_set = set(page)   
    valid = True
    print(pages_set)
    for num in page:
        requirements = tracker[num]
        for requirement in requirements:
            if requirement in pages_set and requirement not in seen:
                valid = False
                break
        seen.add(num)
        if not valid:
            break
    if valid:
        res.append(page[len(page) // 2])
        print(res)
        print(page[len(page) // 2])

print(sum(res))