def verify(data): 

	t = data
	data = data.split(' ')
	hm = {}
	for d in data[1:]: 
		key, value = d.split(':')
		hm[key] = value


	if 'byr' not in hm or  not (1920 <= int(hm['byr']) <= 2002): 
		return False 
	if 'iyr' not in hm or not (2010 <= int(hm['iyr']) <= 2020): 
		return False 
	if 'eyr' not in hm or not (2020 <= int(hm['eyr']) <= 2030): 
		return False 
	if 'hgt' not in hm: return False 
	h = hm['hgt']
	unit = h[-2:]
	num = h[:-2]

	if unit not in ('cm', 'in'):
		print(hm['hgt'])
		return False
	if not num.isdigit():
	   	return False

	n = int(num)

	if unit == 'cm' and not (150 <= n <= 193):
	    return False
	if unit == 'in' and not (59 <= n <= 76):
	    return False
	if ('hcl' not in hm or len(hm['hcl']) != 7 
		or hm['hcl'][0] != '#' or any(c not in '0123456789abcdef' for c in hm['hcl'][1:])):
		return False 
	if 'ecl' not in hm or hm['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}: 
		return False 
	if 'pid' not in hm or not hm['pid'].isnumeric() or len(hm['pid']) != 9: 
		return False


	return True 

ans = 0 

with open('input.txt', 'r') as file: 
	curr = ''
	for line in file: 
		if line == '\n': 
			ans += verify(curr)
			curr = ''
		else: 
			curr += ' ' + line.strip()
if curr: 
	ans += verify(curr)

print(ans)

