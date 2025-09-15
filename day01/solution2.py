from collections import Counter
leftNums = []
rightNums = []

with open("input1.txt", "r+") as f:
    for line in f.readlines():
        left, right = line.strip().split("   ")

        leftNums.append(int(left))
        rightNums.append(int(right))

count = Counter(rightNums)
#print(count)

similarity = 0
for i in range(len(leftNums)):
    similarity += leftNums[i] * count[leftNums[i]]

print(similarity)

#TC: O(n)
#SC: O(n)