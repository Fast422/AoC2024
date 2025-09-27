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
        
        print(self.antennaPositions)
if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()