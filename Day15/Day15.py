grid = []
inputDirs = ""

state = True
with open("Day15.txt", "r") as file:
    for line in file:
        temp = line.strip()
        if temp == "":
            state = False
        if state:
            grid.append(list(temp))
        else:
            inputDirs += temp

ROWS = len(grid)
COLS = len(grid[0])


for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == '@':
            currLocation = (r, c)
            break

dirs = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

for d in inputDirs:

    dx, dy = dirs[d]
    tx, ty = currLocation[0] + dx, currLocation[1] + dy

    if grid[tx][ty] == "#":
        continue
    elif grid[tx][ty] == ".":
        grid[currLocation[0]][currLocation[1]] = '.'
        grid[tx][ty] = '@'
        currLocation = (tx, ty)
        continue
    else:
        sx, sy, = tx, ty

        while grid[tx][ty] == "O":
            tx += dx
            ty += dy

        if grid[tx][ty] == '#':
            continue
        elif grid[tx][ty] == '.':
            grid[sx][sy] = '.'
            grid[tx][ty] = 'O'
            grid[currLocation[0]][currLocation[1]] = '.'
            grid[sx][sy] = '@'
            currLocation = (sx, sy)


ans = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'O':
            ans += 100 * r + c
print(ans)


