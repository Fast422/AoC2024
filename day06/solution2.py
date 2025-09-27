class Solution:
    def __init__(self, input) -> None:
        self.input = input

    def readfile(self):
        with open(self.input, "r") as f:
            lines = [list(line.strip()) for line in f.readlines()]
        
        self.grid = lines
        self.rows, self.cols = len(lines), len(lines[0])

    def printGrid(self):
        for row in self.grid:
            print(row)
    
        
    def findPos(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "^":
                    self.pos = (r, c)
    
    def simulateWalk(self):
        r, c = self.pos
        self.grid[r][c] = "X"
        direction = "up"
        visited = {(r,c)}


        moves = {
            "up":(-1, 0),
            "down":(1, 0),
            "right":(0, 1),
            "left":(0, -1)
        }

        order = ["up", "right", "down", "left"]
        
        while True:
            dr, dc = moves[direction]
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                break
            else:
                if self.grid[nr][nc] not in [".", "X"]:
                    idx = (order.index(direction) + 1) % 4
                    direction = order[idx]
                else:
                    r, c = nr, nc
                    visited.add((r,c))
        return visited

    def simulateWalkWithLoopCheck(self):
        r, c = self.pos
        self.grid[r][c] = "X"
        direction = "up"
        visited = {(r,c, direction)}

        moves = {
            "up":(-1, 0),
            "down":(1, 0),
            "right":(0, 1),
            "left":(0, -1)
        }

        order = ["up", "right", "down", "left"]
        
        while True:
            dr, dc = moves[direction]
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < self.rows and 0 <= nc < self.cols):
                break
            else:
                if self.grid[nr][nc] not in [".", "X"]:
                    idx = (order.index(direction) + 1) % 4
                    direction = order[idx]
                else:
                    r, c = nr, nc
                    if (r,c,direction) in visited:
                        return True
                    else:
                        visited.add((r,c, direction))
        return False       
    
    def run(self):
        self.readfile()
        self.findPos()
        visited = self.simulateWalk()
        counter = 0
        for (r,c) in visited:
            self.grid[r][c] = "#"
            if self.simulateWalkWithLoopCheck():
                counter += 1
            self.grid[r][c] = "."
            print(counter)
        


if __name__ == "__main__":
    solution = Solution("input.txt")
    solution.run()