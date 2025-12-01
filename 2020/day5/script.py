ROWS = 128
COLS = 8 

def Bsearch(left, right, dirs, lowerIndicator): 

	for curr in dirs: 
		mid = (left+right) // 2
		if curr == lowerIndicator: 
			right = mid 
		else: 
			left = mid + 1
	return left if lowerIndicator == 'F' else right


def getSeatId(r, c): 

	row = Bsearch(0, 127, r, 'F')
	col = Bsearch(0, 7, c, 'L')
	return row * 8 + col




l = set()
with open('input.txt', 'r') as file: 
	for line in file: 
		r = line[:7]
		c = line[7:]
		l.add(getSeatId(r, c))


smallest, largest = min(l), max(l)
for n in range(smallest, largest): 
	if n not in ls: 
		print(n)



# for i, j, k in zip(temp[1:], temp[2:], temp[3:]): 
# 	if i+1 == j == k-1: 
# 		print(j)


