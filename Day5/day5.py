from collections import defaultdict, deque

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

def topo(update):

    pages = set(update)

    adj = defaultdict(list)
    in_degree = {p: 0 for p in pages}

    for y in pages:
        for x in rules[y]:
            if x in pages:
                adj[x].append(y)
                in_degree[y] += 1

    q = deque([p for p in pages if in_degree[p] == 0])
    order = []

    while q:
        node = q.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    return int(order[len(order)//2])


ans2 = 0
for update in incorrectUpdates:
   ans2 += topo(update)

print(ans2)