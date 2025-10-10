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
            
            # Process files in descending order (largest index first)
            for file_id in range(max_file_id, -1, -1):
                if file_id % 100 == 0:
                    print(f"Processing file ID: {file_id}")
                
                # Find the current position and size of this file using diskCounts
                file_size = self.diskCounts.get(file_id, 0)
                if file_size == 0:
                    continue
                
                # Find where this file currently is
                file_start = None
                for i in range(len(disk)):
                    if disk[i] == file_id:
                        file_start = i
                        break
                
                if file_start is None:
                    continue
                
                # Try to find a contiguous free space to the left
                free_start = None
                i = 0
                while i < file_start:
                    if disk[i] is None:
                        # Found start of a free space, check if it's big enough
                        free_count = 0
                        j = i
                        while j < file_start and disk[j] is None:
                            free_count += 1
                            j += 1
                        
                        if free_count >= file_size:
                            free_start = i
                            break
                        i = j
                    else:
                        i += 1
                
                # If we found a suitable space, move the file
                if free_start is not None:
                    # Clear the old position
                    for k in range(file_size):
                        disk[file_start + k] = None
                    # Place file in new position
                    for k in range(file_size):
                        disk[free_start + k] = file_id
            
            res.append(self.calculateCheckSum(disk))
            #print(disk)
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
