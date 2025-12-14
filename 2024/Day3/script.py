import re
with open("input.txt", "r") as file:
        s = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
valid_instructions = re.findall(pattern, s)

ans = 0

for x, y in valid_instructions:
    ans += (int(x) * int(y))

print(ans)

pattern2 = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

valid_instructions_2 = re.findall(pattern2, s)
#print(valid_instructions_2)

add = True
findNums = r"(\d{1,3}),(\d{1,3})"
ans2 = 0
for curr in valid_instructions_2:
    if curr == "do()":
        add = True
    elif curr == "don't()":
        add = False
    elif add:
        temp = re.findall(findNums, curr)
        x, y = temp[0]
        ans2 += int(x) * int(y)

print(ans2)