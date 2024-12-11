l = []

with open("Day10.txt", "r") as file:
    for line in file:
        l.append(list(line.strip()))

ROWS = len(l)
COLS = len(l[0])
print(ROWS, COLS)

def dfs(row, col, prevHeight, visited):
    if (row, col) in visited:
        return 0
    if ROWS <= row or row < 0 or COLS <= col or col < 0:
        return 0

    currHeight = int(l[row][col])

    if currHeight - prevHeight != 1:
        return 0

    visited.add((row, col))
    if currHeight == 9:
        return 1
    else:
        return (dfs(row+1, col, currHeight, visited) + dfs(row, col+1, currHeight, visited)
                + dfs(row-1, col, currHeight, visited) + dfs(row, col-1, currHeight, visited))


ans = 0
for i in range(ROWS):
    for j in range(COLS):
        if l[i][j] == '0':
            visited = set()
            ans += dfs(i, j, -1, visited)

print(ans)

#part2


def dfs(row, col, prevHeight, visited):
    if (row, col) in visited:
        return 0
    if ROWS <= row or row < 0 or COLS <= col or col < 0:
        return 0

    currHeight = int(l[row][col])

    if currHeight - prevHeight != 1:
        return 0

    newSet = set(visited)
    newSet.add((row, col))
    if currHeight == 9:
        return 1
    else:
        return (dfs(row + 1, col, currHeight, newSet) + dfs(row, col + 1, currHeight, newSet)
                + dfs(row - 1, col, currHeight, newSet) + dfs(row, col - 1, currHeight, newSet))


ans = 0
for i in range(ROWS):
    for j in range(COLS):
        if l[i][j] == '0':
            visited = set()
            ans += dfs(i, j, -1, visited)

print(ans)