import re

WIDTH = 101
HEIGHT = 103
# robots = []
# for line in open("Day14.txt"):
#     robots.append(tuple(map(int, re.findall(r"-?\d+", line))))
#
# res = []
# for px, py, vx, vy in robots:
#     res.append(((px + vx * 100) % WIDTH, (py + vy * 100)% HEIGHT))
#
# VM = (HEIGHT-1) // 2
# HM = (WIDTH-1) // 2
#
#
# tl = tr = bl = br = 0
# for px, py in res:
#     if px == HM or py == VM: continue
#
#     if px > HM:
#         if py < VM:
#             tr += 1
#         else:
#             br += 1
#     else:
#         if py < VM:
#             bl += 1
#         else:
#             tl += 1
#
# print(tr * tl * bl * br)



#part 2

VM = (HEIGHT-1) // 2
HM = (WIDTH-1) // 2

robots = []
for line in open("Day14.txt"):
    robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

min_sf = float("inf")
best_iter = None

for second in range(WIDTH * HEIGHT):
    res = []
    for px, py, vx, vy in robots:
        res.append(((px + vx * second) % WIDTH, (py + vy * second) % HEIGHT))


    tl = tr = bl = br = 0
    for px, py in res:
        if px == HM or py == VM: continue

        if px > HM:
            if py < VM:
                tr += 1
            else:
                br += 1
        else:
            if py < VM:
                bl += 1
            else:
                tl += 1

    sf = (tr * tl * bl * br)

    if sf < min_sf:
        min_sf = sf
        best_iter = second

print(best_iter)