class Solution:
    def parse(self):
        with open("input.txt", "r") as f:
            self.lines = [line.replace(":", "").strip().split(" ") for line in f.readlines()]
    
    def solve(self):
        values = []
        for equation in self.lines:
            equation = list(map(int, equation))
            target = equation[0]
            equation = equation[1:]
            #print(equation, target)
            def dfs(i, c):
                #print(i,c)
                if i == len(equation):
                    return c == target

                return dfs(i+1, c+equation[i]) or dfs(i+1, c*equation[i])
            if dfs(1, equation[0]):
                values.append(target)
        print(sum(values))

if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()