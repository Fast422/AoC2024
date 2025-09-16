import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

grid = np.array([list(line) for line in lines])

rows, cols = grid.shape
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def dfs(r, c, searched, direction = None):
    target = ["X", "M", "A", "S"]

    if searched != target[:len(searched)]:
        return 0

    #If we've found the word
    if len(searched) == 4:
        if searched == ["X", "M", "A", "S"]:
            return 1
        return 0
    count = 0
    if not direction:
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                count += dfs(nr, nc, searched + [grid[nr, nc]], direction = (dr, dc))
        return count
    
    if direction and searched:
        dr, dc = direction
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            count += dfs(nr, nc, searched + [grid[nr, nc]], direction = (dr, dc))
        return count
    
    return count
    

count = 0
for r in range(rows):
    for c in range(cols):
        if grid[r, c] in ["X"]:
            count += dfs(r, c, [grid[r,c]])

print(count)

#TC: O(n^2) where N is the size of the grid (assuming square grid)
#SC: O(1)