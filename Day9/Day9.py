

with open("Day9.txt", "r") as file:
    for line in file:
        s = line.strip()

arr = []

for i, n in enumerate(s):
    if i % 2 == 0:
        currVal = i // 2
        temp = [currVal] * int(n)
    else:
        temp = ['.'] * int(n)

    for j in temp:
        arr.append(j)


left = 0
right = len(arr) - 1

while left < right:
    if arr[left] != '.':
        left += 1
    elif arr[right] == '.':
        right -= 1
    else:
        arr[left] = arr[right]
        left += 1
        right -= 1

ans = 0
for i, n in enumerate(arr[:right+1]):
    ans += int(i) * n

print(ans)


# #part2
#
# arr2 = []
# for i, n in enumerate(s):
#     if i % 2 == 0:
#         currVal = i // 2
#         temp = [currVal] * int(n)
#     else:
#         temp = ['.'] * int(n)
#
#     if len(temp) > 0:
#         arr2.append(temp)
#
#
# i = len(arr2) -1
#
# while i >= 0:
#     right = arr2[i]
#     if right[0] == '.':
#         i -= 1
#         continue
#     for j in range(i):
#         left = arr2[j]
#         if left[0] != '.':
#             continue
#         elif len(left) >= len(right):
#             arr2.pop(j)
#             arr2.insert(j, right)
#             if len(left) > len(right):
#                 arr2.insert(j + 1, ['.'] * (len(left) - len(right)))
#                 i += 1
#
#             arr2[i] = ['.' for _ in right]
#             temp = i
#             if i+1 < len(arr2) and arr2[i+1][0] == '.':
#                 for _ in range(len(arr2[i+1])):
#                     arr2[i].append('.')
#                 arr2.pop(i+1)
#                 i -= 1
#
#
#             if temp - 1 >= 0 and arr2[temp - 1][0] == '.':
#                 for _ in range(len(arr2[temp - 1])):
#                     arr2[temp].append('.')
#                 arr2.pop(temp - 1)
#                 i -= 1
#
#             break
#     i -= 1
#
# ans2 = 0
# s = ""
# for i in range(len(arr2)):
#     for j in range(len(arr2[i])):
#         s += str(arr2[i][j])
#         if arr2[i][j] != '.':
#             ans2 += j * int(arr2[i][j])
# print(ans2)
# print(s)

files = [] # (start, length)
blanks = []
pos = 0

with open("Day9.txt", "r") as file:
    for line in file:
        s = line.strip()
        for i, n in enumerate(list(s)):
            x = int(n)
            if i % 2 == 0:
                files.append([pos, x])
            else:
                if x != 0:
                    blanks.append([pos, x])
            pos += x


for i, file in enumerate(files[::-1]):
    i = len(files) - i - 1
    start, length = file

    for j, blank in enumerate(blanks):
        blankStart, blankLength = blank

        if start < blankStart:
            break
        elif length > blankLength:
            continue
        else:
            files[i][0] = blankStart
            if length == blankLength:
                blanks.pop(j)
            else:
                blanks[j][0] = blankStart + length
                blanks[j][1] = blankLength - length
            break

ans2 = 0
for i, (start, length) in enumerate(files):
    for x in range(start, start + length):
        ans2 += i * x

print(ans2)