from collections import Counter

l = []

with open("day4.txt", "r") as file:
    for line in file:
        l.append(list(line))

ROWS = len(l)
COLS = ROWS


def searchLeft(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col - i < 0 or s[i] != l[row][col - i]:
            return False
    return True


def searchRight(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col + i >= COLS or s[i] != l[row][col + i]:
            return False
    return True


def searchUp(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if row - i < 0 or s[i] != l[row - i][col]:
            return False
    return True


def searchDown(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if row + i >= ROWS or s[i] != l[row + i][col]:
            return False
    return True


def searchDownLeft(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col - i < 0 or row + i >= ROWS or s[i] != l[row + i][col - i]:
            return False
    return True


def searchDownRight(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col + i >= COLS or row + i >= ROWS or s[i] != l[row + i][col + i]:
            return False
    return True


def searchUpLeft(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col - i < 0 or row - i < 0 or s[i] != l[row - i][col - i]:
            return False
    return True


def searchUpRight(row, col):
    s = ('X', 'M', 'A', 'S')
    for i in range(4):
        if col + i >= COLS or row - i < 0 or s[i] != l[row - i][col + i]:
            return False
    return True

def search(row, col):
    if row + 1 >= ROWS or row - 1 < 0 or col + 1 >= COLS or col - 1 < 0:
        return False
    c = [l[row + 1][col + 1], l[row + 1][col - 1], l[row - 1][col + 1], l[row - 1][col - 1]]
    temp = Counter(c)
    if temp['S'] == 2 and temp['M'] == 2 and c[0] != c[3]:
        return True
    return False


counter = 0
counter2 = 0
for row in range(ROWS):
    for col in range(COLS):
        counter += (searchLeft(row, col) + searchRight(row, col) + searchUp(row, col) + searchDown(row, col)
                    + searchUpRight(row, col) + searchUpLeft(row, col) + searchDownRight(row, col)
                    + searchDownLeft(row, col))
        if l[row][col] == 'A':
            counter2+= search(row, col)
print(counter)
print(counter2)

# part2


