leftNums = []
rightNums = []

with open("input1.txt", "r+") as f:
    for line in f.readlines():
        left, right = line.strip().split("   ")

        leftNums.append(int(left))
        rightNums.append(int(right))

leftNums.sort()
rightNums.sort()
# print(leftNums[:10])
# print(rightNums[:10])

total = 0

for i in range(len(leftNums)):
    total += abs(leftNums[i] - rightNums[i])

print(total)

#Time Complexity: O(nlog(n))
#Space Complexity: O(n)