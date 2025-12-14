from collections import Counter

list1 = []
list2 = []

with open("input.txt", "r") as file:
    for line in file:
        temp = line.strip().split()
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))




def Part1(): 
    list1.sort()
    list2.sort()
    return sum(abs(l - r) for l, r in zip(list1, list2))

def Part2(): 
    F = Counter(list2)
    return sum(n * F[n] for n in list1)

print(Part2())
print(Part1())