def isValidOne(lower, upper, letter, string):

    count = string.count(letter)
    return lower <= count <= upper

def isValidTwo(i, j, letter, string):

    if string[i-1] == string[j-1]: return False

    return string[i-1] == letter or string[j-1] == letter

ans1 = 0 
ans2 = 0 


with open("input.txt", "r") as file:
    for line in file:
        s = line.strip().split(' ')
        lower, upper = s[0].split('-')
        lower, upper = int(lower), int(upper)
        letter = s[1][0]
        string = s[2]

        ans1 += isValidOne(lower, upper, letter, string)
        ans2 += isValidTwo(lower, upper, letter, string)

print(ans1, ans2)

        
