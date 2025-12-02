
# input
data = [] 

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()
		ranges = line.split(',')
		for r in ranges: 
			a, b = r.split('-')
			a, b = int(a), int(b)
			data.append((a, b)) 

def Part1(data): 

	ans = 0

	for a, b in data: 
		for i in range(a, b+1):
		
			strRep = str(i)
			lenStrRep = len(strRep)
			if lenStrRep % 2 != 0: 
				continue 

			if strRep[:lenStrRep//2] == strRep[lenStrRep//2:]: 
				ans += i

	return ans


def Part2(data): 
	ans = 0

	for a, b in data: 
		for i in range(a, b+1):
		
			strRep = str(i)
			for j in range(1, len(strRep)): 
				curr = strRep[:j]
				count = strRep.count(curr)
				if count * j == len(strRep): 
					ans += i 
					break 
					

	return ans


print(Part1(data))
print(Part2(data))