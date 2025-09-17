from collections import defaultdict

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

separator_idx = lines.index("")
instructions = lines[:separator_idx]
pages = [list(map(int, line.split(","))) for line in lines[separator_idx+1:]]

# print(instructions)
# print(pages)
tracker = defaultdict(list)
global_graph = defaultdict(list)

for instruction in instructions:
    before, after = map(int, instruction.split("|"))
    tracker[after].append(before)
    global_graph[before].append(after)

def reorder_pages(pages):
    #Re-ordering
    graph = defaultdict(list)
    numbers = set(pages)
    #print(f"Set of numbers: {numbers}")
    for number in numbers:
        all_dependencies = global_graph[number]
        #print(f"All dependencies for {number}: {all_dependencies}")
        required_dependencies = [x for x in all_dependencies if x in numbers]
        print(f"Required dependencies for {number}: {required_dependencies}")
        graph[number] = required_dependencies
        #Pull out only the ones that are needed in the graph
    print(graph)

    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                dfs(v)
        stack.append(u)

    for u in pages:
        if u not in visited:
            dfs(u)
    order = stack[::-1]
    print(order)
    mid = order[len(order) // 2]
    return mid

res = 0
for page in pages:
    seen = set()  
    pages_set = set(page)   
    valid = True
    #print(pages_set)
    for num in page:
        requirements = tracker[num]
        for requirement in requirements:
            if requirement in pages_set and requirement not in seen:
                valid = False
                break
        seen.add(num)
        if not valid:
            break
    if not valid:
        res += reorder_pages(page)

print(res)
