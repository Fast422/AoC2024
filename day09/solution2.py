class Solution:
    def parse(self):
        with open("input.txt", "r+") as f:
            self.lines = [line.strip() for line in f.readlines()]
            #print(self.lines)

        
        self.diskCounts = {}
        self.diskMaps = []
        for line in self.lines:
            disk = []
            for i in range(len(line)):
                if i % 2 == 0:
                    # Add file blocks with file ID
                    disk.extend([i//2] * int(line[i]))
                    self.diskCounts[i//2] = int(line[i])
                else:
                    # Add empty spaces (represented as None)
                    disk.extend([None] * int(line[i]))
            self.diskMaps.append(disk)
        print(self.diskMaps)
    def solve(self):
        res = []
        for disk in self.diskMaps:
            disk = list(disk)
            
            # Get the max file ID
            max_file_id = max(id for id in disk if id is not None)
            print(f"Processing {max_file_id + 1} files, disk size: {len(disk)}")
            min_file_id = min(id for id in disk if id is not None)
            # Process files in descending order (largest index first)
            for file_id in range(max_file_id, min_file_id-1, -1):
                if file_id % 100 == 0:
                    print(f"Processing file ID: {file_id}")
                file_size = self.diskCounts.get(file_id, 0)
                if file_size == 0:  # Skip files with size 0
                    continue

                if file_id not in disk:  # Skip if file not in disk
                    continue
                current_location = disk.index(file_id)
                i = 0
                #Look for space
                while i < current_location:
                    if disk[i] == None:
                        j = i + 1
                        space = 1
                        while j < len(disk) and not disk[j]:
                            space += 1
                            j += 1
                        
                        if space >= file_size:
                            for k in range(file_size):
                                disk[current_location + k] = None
                            for k in range(file_size):
                                disk[i + k] = file_id
                            break
                        i = j  # Skip the space we just checked and continue
                    else:
                        i += 1
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
