class Solution:
    def __init__(self, input) -> None:
        self.input = input

    def readfile(self):
        with open(self.input, "r") as f:
            lines = [list(line.strip()) for line in f.readlines()]
        
        self.grid = lines
        self.rows, self.cols = len(lines), len(lines[0])

        print(self.grid)
        print(self.rows)
        print(self.rows)
        
    def findPos(self):
        pass


if __name__ == "__main__":
    solution = Solution("input.txt")
    solution.readfile()