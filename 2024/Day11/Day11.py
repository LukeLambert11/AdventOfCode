with open("Day11.txt", "r") as file:
    for line in file:
        l = line.strip().split()

l = [int(i) for i in l]
prev = 0
part2 = l.copy()

for _ in range(25):
    length = len(l)
    for i in range(length):
        curr = l[i]

        if curr == 0:
            l[i] = 1
        elif len(str(curr)) % 2 == 0:
            tempLength = len(str(curr))
            left = int(str(curr)[0:tempLength // 2])
            right = int(str(curr)[tempLength // 2:])
            l[i] = left
            l.append(right)
        else:
            l[i] = curr * 2024
    prev = len(l)

print(len(l))

cache = {}


def ans(num, iter):
    if iter == 0:
        return 1

    if (num, iter) not in cache:

        if num == 0:
            result = ans(1, iter - 1)

        elif len(str(num)) % 2 == 0:
            tempLength = len(str(num))
            result = 0
            left = int(str(num)[0:tempLength // 2])
            right = int(str(num)[tempLength // 2:])
            result += ans(left, iter - 1)
            result += ans(right, iter - 1)
        else:
            result = ans(2024 * num, iter - 1)
        cache[(num, iter)] = result
    return cache[(num, iter)]


ans2 = 0
for x in part2:
    ans2 += ans(x, 75)
print(ans2)
