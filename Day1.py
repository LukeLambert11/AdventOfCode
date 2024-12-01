from collections import Counter

list1 = []
list2 = []

with open("day1.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

c = Counter(list2)


#list1.sort()
#list2.sort()
#print(sum(abs(l - r) for l, r in zip(list1, list2)))



ans = sum(i * c[i] for i in list1)
print(ans)