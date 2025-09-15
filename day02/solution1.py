reports = []
with open("input1.txt", "r+") as f:
    for line in f.readlines():
        report = [int(x) for x in line.strip().split(" ")]
        reports.append(report)

safe = 0
for report in reports:

    is_asc = True
    is_desc = True
    for i in range(len(report) - 1):
        if report[i] < report[i+1]:
            is_desc = False
        if report[i] > report[i+1]:
            is_asc = False
    
    first_test = is_asc or is_desc

    second_test = True
    for i in range(len(report)-1):
        diff = abs(int(report[i]) - int(report[i+1]))
        if not 1 <= diff <= 3:
            second_test = False
            break

    print(f"First Test: {first_test} \nSecond Test: {second_test}")
    if first_test and second_test:
        safe += 1

print(safe)

#TC: O(n)
#SC: O(n)