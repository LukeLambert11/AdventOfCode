from collections import defaultdict
from math import gcd

l = []

with open("Day8.txt", "r") as file:
    for line in file:
        temp = line.strip()
        l.append(list(temp))


ROWS = len(l)
COLS = len(l[0])
print(ROWS, COLS)
antennas = defaultdict(set)
for temp in l:
    print(temp)

for row in range(len(l)):
    for col in range(len(l[0])):
        val = l[row][col]
        if val != '.':
            antennas[val].add((row, col))

print(antennas)

visited = set()

for a in antennas:
    curr = list(antennas[a])
    for i in range(len(curr)):
        for j in range(i+1, len(curr)):
            x1, y1 = curr[i]
            x2, y2 = curr[j]

            P1 = (2 * x2 - x1, 2 * y2 - y1)
            P2 = (2 * x1 - x2, 2 * y1 - y2)


            if 0 <= P1[0] < ROWS and 0 <= P1[1] < COLS:
                visited.add(P1)
            if 0 <= P2[0] < ROWS and 0 <= P2[1] < COLS:
                visited.add(P2)

print(len(visited))

visited2 = set()
for a in antennas:
    curr = list(antennas[a])
    for i in range(len(curr)):
        for j in range(i+1, len(curr)):
            x1, y1 = curr[i]
            x2, y2 = curr[j]
            rise = y2 - y1
            run = x2 - x1

            tempX, tempY = x1, y1

            while 0 <= tempX < ROWS and 0 <= tempY < COLS:
                visited2.add((tempX, tempY))
                tempX += run
                tempY += rise

            tempX, tempY = x1, y1
            while 0 <= tempX < ROWS and 0 <= tempY < COLS:
                visited2.add((tempX, tempY))
                tempX -= run
                tempY -= rise

print(len(visited2))



