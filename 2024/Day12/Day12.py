l = []
with open("Day12.txt", "r") as file:
    for line in file:
        l.append([i for i in line.strip()])

print(l)

ROWS = len(l)
COLS = len(l[0])

visited = set()

def dfs(row, col, crop):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return 0, 1

    if l[row][col] != crop:
        return 0, 1

    if (row, col) in visited:
        return 0, 0

    visited.add((row, col))

    area, perimeter = 1, 0

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in dirs:
        a, p = dfs(row+x, col+y, crop)
        area += a
        perimeter += p

    return area, perimeter

ans = 0
for row in range(ROWS):
    for col in range(COLS):
        a, p = dfs(row, col, l[row][col])
        ans += a * p

print(ans)


#part 2


