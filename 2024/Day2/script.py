l = []

with open("input.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        l.append(list(map(int, temp)))


def helper(report, un_safe):
    dir = 1 if report[1] - report[0] > 0 else -1
    curr = report[0]

    for a, b in zip(report, report[1:]):
        diff = (b - a) * dir
        if diff <= 0 or diff > 3:
            un_safe.append(report)
            return False
    return True


ans1 = 0
un_safe = []
for report in l:
    ans1 += helper(report, un_safe)
print(ans1)

ans2 = 0
useless = []
for report in un_safe:
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        if helper(temp, useless):
            ans2 += 1
            break

print(ans1 + ans2)