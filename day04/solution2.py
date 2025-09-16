import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f]

grid = np.array([list(line) for line in lines])

rows, cols = grid.shape
direction1 = [(-1, -1), (0, 0), (1, 1)]
direction2 = [(-1, 1), (0, 0), (1, -1)]

count = 0
for r in range(1, rows-1):
    for c in range(1, cols-1):
        if grid[r, c] == "A":
            dir1 = []
            for direction in direction1:
                dr, dc = direction
                dir1.append(grid[r+ dr, c + dc])
            
            dir2 = []
            for direction in direction2:
                dr, dc = direction
                dir2.append(grid[r+dr, c+dc])

            if dir1 in [["M", "A", "S"], ["S", "A", "M"]] and dir2 in [["M", "A", "S"], ["S", "A", "M"]]:
                count += 1

print(count)

#TC: O(n)
#SC: O(1)