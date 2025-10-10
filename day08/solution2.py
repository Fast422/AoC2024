from collections import defaultdict
class Solution:
    def parse(self):
        with open("input.txt", "r") as f:
            self.grid = [list(line.strip()) for line in f.readlines()]
        
        # for row in self.grid:
        #     print(f"{row}\n")
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
    def solve(self):
        self.antennaPositions = defaultdict(list)
        self.occupied = set()
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] != ".":
                    self.occupied.add((r,c))
                    char = self.grid[r][c]
                    self.antennaPositions[char].append((r,c))
        
        print(self.antennaPositions.values())
        self.antinodes = set()
        for values in self.antennaPositions.values():
            for i in range(len(values)):
                c1 = values[i]
                for j in range(i+1, len(values)):
                    c2 = values[j]
                    for e in self.findAntiNodePosition(c1,c2):
                        self.antinodes.add(e)
        print(len(self.antinodes))

    
    def findAntiNodePosition(self, c1, c2):
        res = []
        x1, y1 = c1
        x2, y2 = c2

        dx1 = x1-x2
        dy1 = y1-y2

        dx2 = x2-x1
        dy2 = y2-y1
        
        while self.valid(c1):
            res.append(c1)
            x1 += dx1
            y1 += dy1
            c1 = (x1, y1)

        while self.valid(c2):
            res.append(c2)
            x2 += dx2
            y2 += dy2
            c2 = (x2, y2)
        return res
    
    def valid(self, c):
        x, y = c
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return True
        return False
if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()