class Solution:
    def parse(self):
        with open("input.txt", "r+") as f:
            self.lines = [line.strip() for line in f.readlines()]
            #print(self.lines)
        
        self.diskMaps = []
        for line in self.lines:
            disk = []
            for i in range(len(line)):
                if i % 2 == 0:
                    # Add file blocks with file ID
                    disk.extend([i//2] * int(line[i]))
                else:
                    # Add empty spaces (represented as None)
                    disk.extend([None] * int(line[i]))
            self.diskMaps.append(disk)
        #print(self.diskMaps)
    def solve(self):
        res = []
        for disk in self.diskMaps:
            disk = list(disk)
            l = 0
            r = len(disk) - 1
            # Find the rightmost file block
            while r >= 0 and disk[r] is None:
                r -= 1

            while True:
                # find next left hole
                while l < len(disk) and disk[l] is not None:
                    l += 1
                # find next right file block
                while r >= 0 and disk[r] is None:
                    r -= 1
                if l >= r:
                    break
                # swap them
                disk[l], disk[r] = disk[r], None
                l += 1
                r -= 1
            res.append(self.calculateCheckSum(disk))
        print(res)

    def calculateCheckSum(self, s):
        checksum = 0
        for i in range(len(s)):
            if s[i] is not None:
                checksum += s[i] * i
                
        return checksum

if __name__ == "__main__":
    sol = Solution()
    sol.parse()
    sol.solve()
