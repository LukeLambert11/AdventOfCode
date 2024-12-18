from collections import deque, defaultdict
from copy import deepcopy

l = []
l.append(['?'] * 130)
#should just use .strip() but commited to it like this today
with open("Day6.txt", "r") as file:
    for i, line in enumerate(file):
        for j, char in enumerate(line):
            if char == '^':
                guard_location = [i+1, j+1]

        l.append(list('?' + line[:-1] + '?'))
l.append(['?'] * 130)

for temp in l:
    print(temp)
g = deepcopy(l)

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
path = []
curr_index = 0
counter = 0
inMap = True

while inMap:

    row, col = moves[curr_index]

    next_grid = l[guard_location[0] + row][guard_location[1] + col]

    if next_grid == '?':
        inMap = False
    elif next_grid == '#':
        curr_index = (curr_index + 1) % 4
    else:
        path.append((guard_location[0], guard_location[1], curr_index))
        guard_location[0] += row
        guard_location[1] += col
        if next_grid == '.' or next_grid == '^':
            l[guard_location[0]][guard_location[1]] = 'X'
            counter += 1



print(counter)



def helper(grid, guard_location, curr_index):

    visited = set()

    while True:
        # for t in grid:
        #     print(t)
        row, col = moves[curr_index]

        next_grid = grid[guard_location[0] + row][guard_location[1] + col]

        if next_grid == '?':
            return False
        elif next_grid == '#':
            curr_index = (curr_index + 1) % 4
        else:
            if (guard_location[0], guard_location[1], curr_index) in visited:
                return True
            else:
                visited.add((guard_location[0], guard_location[1], curr_index))
            guard_location[0] += row
            guard_location[1] += col
            if next_grid == '.' or next_grid == '^':
                grid[guard_location[0]][guard_location[1]] = 'Y' #Y easier for testing

ans2 = 0

# #cannot place right in front of start so start from 1
# for loc in path[1:]:
#     # print("\n\n")
#     row, col, index = loc
#     # print(row, col, index)
#     temp = deepcopy(g)
#     temp[row + moves[index][0]][col + moves[index][1]] = "#"
#
#
#     ans2 += helper(temp, [row, col], index)

for i in range(1, len(g) - 1):
    for j in range(1, len(g[i]) - 1):
        if (i, j) != (path[0][0], path[0][1]) and g[i][j] == '.':
            # Make a copy of the original grid
            temp = deepcopy(g)
            # Place a new obstruction here
            temp[i][j] = '#'

            # Test if this causes a loop when starting from the original state
            if helper(temp, [path[0][0], path[0][1]], 0):
                ans2 += 1

print(ans2)

