class Solution:
    def parse(self):
        with open("input.txt", "r") as f:
            self.grid = [line.strip() for line in f.readlines()]
        # for line in self.lines:
        #     print(line)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def solve(self):
        self.starts = set()

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == "0":
                    self.starts.add((r,c))
        
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        self.score = 0

        def findScore(r, c, visited):
            
        

if __name__ == "__main__":
    sol = Solution()
    sol.parse()
