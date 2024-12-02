
l = []

with open("day2.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        l.append([int(i) for i in temp])

unSafe = []
ans = 0
for report in l:

    multi = 1 if report[1] - report[0] > 0 else -1
    curr = report[0]

    temp_bool = True
    for num in report[1:]:
        is_valid = (num - curr) * multi
        curr = num
        if 0 >= is_valid or is_valid > 3:
            temp_bool = False
            break
    if not temp_bool:
        unSafe.append(report)
    ans += temp_bool

print(ans)


def helper(newReport):
    multi = 1 if newReport[1] - newReport[0] > 0 else -1
    curr = newReport[0]

    for num in newReport[1:]:
        is_valid = (num - curr) * multi
        curr = num
        if 0 >= is_valid or is_valid > 3:
            print(newReport)
            return False
    print("true", newReport)

    return True

ans2 = 0
for report in unSafe:
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        if helper(temp):
            ans2+= 1
            break

print(ans2 + ans)



