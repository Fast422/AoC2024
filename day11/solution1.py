class Solution:
    def parse(self):
        with open("input.txt", "r") as f:
            self.line = list(map(int, f.readline().strip().split(" ")))

        print(self.line)
    def solve(self):
        for _ in range(25):
            res = []
            for stone in self.line:
                if stone == 0:
                    res.append(1)
                elif len(str(stone)) % 2 == 0:
                    stone = str(stone)
                    left, right = stone[:len(stone)//2], stone[len(stone)//2:]
                    res.append(int(left))
                    res.append(int(right))
                else:
                    res.append(stone*2024)
            self.line = res
            print(len(self.line))
if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()
