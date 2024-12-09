

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


#part2

arr2 = []
for i, n in enumerate(s):
    if i % 2 == 0:
        currVal = i // 2
        temp = [currVal] * int(n)
    else:
        temp = ['.'] * int(n)

    if len(temp) > 0:
        arr2.append(temp)

#print(arr2)


# left = 0
# right = len(arr) - 1
#
# for i, right in enumerate(arr2[::-1]):
#     if right[0] == '.':
#         continue
#     for j, left in enumerate(arr2[:len(arr2) - i]):
#         if left[0] != '.':
#             continue
#         elif len(left) >= len(right):
#             print(arr2.pop(j), right)
#             arr2.insert(j, right)
#             if len(left) > len(right):
#                 arr2.insert(j + 1, ['.'] * (len(left) - len(right)))
#             #print("test", arr2[len(arr2) - i - 1], len(arr2), len(arr2) - i - 1)
#             t = len(arr2) - i - 1
#             while arr2[t] != right:
#                 t -= 1
#
#             arr2[t] = ['.' for _ in right]
#             print("new: ", arr2)
#             break



i = len(arr2) -1

while i >= 0:
    right = arr2[i]
    if right[0] == '.':
        i -= 1
        continue
    for j in range(i):
        left = arr2[j]
        if left[0] != '.':
            continue
        elif len(left) >= len(right):
            arr2.pop(j)
            arr2.insert(j, right)
            if len(left) > len(right):
                arr2.insert(j + 1, ['.'] * (len(left) - len(right)))
                i += 1
            arr2[i] = ['.' for _ in right]
            break
    i -= 1

# Flatten `arr2` into a string
newArr = "".join(str(m) if m != '.' else '.' for n in arr2 for m in n)

# Calculate the checksum
ans2 = sum(i * int(n) for i, n in enumerate(newArr) if n != '.')

s = 0
for i, n in enumerate(newArr):
    if n != '.':
        s += int(n) * i
        print(int(n) * i, n, i)
print(ans2)

