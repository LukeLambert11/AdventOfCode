from collections import defaultdict
import itertools

rules = defaultdict(set)
updates = []

readRules = True
with open("day5.txt", "r") as file:
    for line in file:
        if line.strip() == "":
            readRules = False
            continue

        if readRules:
            temp = line.strip().split('|')
            rules[temp[1]].add(temp[0]) #a set of pages that must be before //cannot be after
        else:
            updates.append(line.strip().split(','))
incorrectUpdates = []

ans = 0


def checkValid(update):
    isValid = True
    for i, page in enumerate(update):

        isValid = all(postPage not in rules[page] for postPage in update[i + 1:])

        if not isValid:
            #
            break
    return int(update[len(update) // 2]) if isValid else 0


for update in updates:
    curr = checkValid(update)
    if curr == 0:
        incorrectUpdates.append(update)
    else:
        ans += curr


print(ans)

#way too slow did not realize the length can be > 5
ans2 = 0
for update in incorrectUpdates:
    permutations = list(itertools.permutations(update))
    curr = 0
    for perm in permutations:
        curr = checkValid(perm)
        if curr != 0:
            ans2 += curr
            break
print(ans2)
