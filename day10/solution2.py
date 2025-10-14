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
        print(self.starts)
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def findScore(r, c, visited):
            if self.grid[r][c] == "9":
                return 1

            total = 0
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in visited and self.grid[nr][nc] == str(int(self.grid[r][c]) + 1):
                    visited.add((nr, nc))
                    total += findScore(nr, nc, visited.copy())
            return total
        
        self.total = 0
        for r, c in self.starts:
            rating = findScore(r, c, set()) 
            print(rating)
            self.total += rating
        print(self.total)
        

if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()
