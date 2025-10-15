import sys
from functools import lru_cache
sys.set_int_max_str_digits(0) 

class Solution:
    def parse(self):
        with open("input.txt", "r") as f:
            self.line = list(map(int, f.readline().strip().split(" ")))

        print(self.line)
    def solve(self):
        @lru_cache(None)
        def count(x, steps):
            if steps == 0:
                return 1
            elif x == 0:
                return count(1, steps-1)
            if len(str(x)) % 2 == 0:
                s = str(x)
                mid = len(s) // 2
                return count(int(s[:mid]), steps-1) + count(int(s[mid:]), steps-1)
            return count(x * 2024, steps - 1)

        total = 0
        for stone in self.line:
            total += count(stone, 75)
        print(total)
if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()
