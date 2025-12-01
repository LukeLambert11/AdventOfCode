


data = []

currMask, currMem = None, []

with open('input.txt', 'r') as file: 
	for line in file: 
		line = line.strip()

		if line.startswith('mask'): 
			if currMask: 
				data.append((currMask, currMem))
				currMem = []
			currMask = line[7:]
		else: 
			addr = int(line[line.find("[")+1 : line.find("]")])
			val = int(line.split(" = ")[1])
			currMem.append((addr, val))

data.append((currMask, currMem))

def ToBinArray(val):
	arr = list(bin(val)[2:])

	leftOver = [0] * (36 - len(arr))
	arr = leftOver + arr
	return arr

def BuildPermutations(addr): 
	perms = []
	indexs = [i for i, n in enumerate(addr) if n == 'X']

	def f(index, addr): 
		if index == len(indexs): 
			perms.append(addr.copy())
			return

		i = indexs[index]
		addr[i] = 0
		f(index+1, addr)

		addr[i] = 1
		f(index+1, addr)

	f(0, addr)
	return perms



def Part1(data): 
	mem = {}

	for mask, ins in data: 
		for addr, val in ins: 
			val = ToBinArray(val)
			for i, n in enumerate(mask): 
				if n == '1': 	
					val[i] = 1
				if n == '0': 
					val[i] = 0 
			binString = ''.join(map(str, val))
			intVal = int(binString, 2)
			mem[addr] = intVal 

	return sum(mem.values())

def Part2(data): 
	mem = {}

	for mask, ins in data: 
		for addr, val in ins: 
			addr = ToBinArray(addr)
			for i, n in enumerate(mask): 
				if n == '1': 
					addr[i] = 1
				if n == 'X': 
					addr[i] = 'X'
			perms = BuildPermutations(addr)
			for a in perms: 
				addrString = ''.join(map(str, a))
				addrVal = int(addrString, 2)
				mem[addrVal] = val 

	return sum(mem.values())

print(Part1(data))
print(Part2(data))


			

