l = []

with open("day2.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        l.append([int(i) for i in temp])


def helper(report, un_safe):
    multi = 1 if report[1] - report[0] > 0 else -1
    curr = report[0]

    for num in report[1:]:
        is_valid = (num - curr) * multi
        curr = num
        if 0 >= is_valid or is_valid > 3:
            un_safe.append(report)
            return False
    return True


ans1 = 0
un_safe = []
for report in l:
    ans1 += helper(report, un_safe)

ans2 = 0
useless = []
for report in un_safe:
    for i in range(len(report)):
        temp = report[:i] + report[i + 1:]
        if helper(temp, useless):
            ans2 += 1
            break

print(ans1 + ans2)

