import re

total = 0

for block in open("Day13.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))

    m = float("inf")
    for i in range(101):
        for j in range(101):

            if ax * i + bx * j == px and ay * i + by * j == py:
                m = min(m, i * 3 + j)

    if m != float("inf"):
        total += m

print(total)


#part 2

total = 0
for block in open("Day13.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    px += 10000000000000
    py += 10000000000000

    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx

    if ca % 1 == 0 and cb % 1 == 0:
        total += int(ca * 3 + cb)

print(total)







