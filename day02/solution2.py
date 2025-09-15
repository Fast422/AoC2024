reports = []
with open("input1.txt", "r+") as f:
    for line in f.readlines():
        report = [int(x) for x in line.strip().split(" ")]
        reports.append(report)

def isSafe(report):
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
    
    return first_test and second_test

def isSafeWithDampener(report):

    if isSafe(report):
        return True
    
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if isSafe(new_report):
            return True
    
    return False

safe = 0
for report in reports:
    if isSafeWithDampener(report):
        safe += 1

print(safe)
