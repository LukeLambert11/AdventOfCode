l = []

with open("Day7.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        temp[0] = temp[0][:-1]
        temp = [int(i) for i in temp]
        l.append(temp)


def findMulti(n):
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return 10 ** c
def dfs(target, value, index, arr):

    if index == len(arr) - 1:
        if target == value:
            return True
        else:
            return False
    if value > target:
        return False

    return dfs(target, value * arr[index+1], index+1, arr) or dfs(target, value + arr[index+1], index+1, arr)


def dfs2(target, value, index, arr):

    if index == len(arr) - 1:
        if target == value:
            return True
        else:
            return False
    if value > target:
        return False

    return (dfs2(target, value * arr[index+1], index+1, arr) or dfs2(target, value + arr[index+1], index+1, arr) or
        dfs2(target, value * findMulti(arr[index+1]) + arr[index+1], index+1, arr))

ans = 0
wrong = []
for row in l:
    if dfs(row[0], row[1], 1, row):
        ans += row[0]
    else:
        wrong.append(row)

print(ans)

for row in wrong:
    if dfs2(row[0], row[1], 1, row):
        ans += row[0]

print(ans)