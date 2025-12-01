

nums = []

with open('input.txt', 'r') as file: 

	for line in file: 
		nums.append(int(line))


def check(nums, index): 
	target = nums[index]

	for i in range(index-25, index): 
		for j in range(i, index): 
			if nums[i] + nums[j] == target: 
				return True 

	return False


def part1(nums): 

	for i, n in enumerate(nums[25:], start=24): 
		
		if not check(nums, i): 
			return nums[i]

def part2(nums, target):
	prefix = [0]
	for n in nums: 
		prefix.append(prefix[-1] + n)

	for i, p in enumerate(prefix): 
		for j, remove in enumerate(prefix[:i]): 
			if p - remove == target: 
				return min(nums[j:i]) + max(nums[j:i])
			if p - remove < target: 
				break 

	return - 1


target = part1(nums)
print(target)
print(part2(nums, target))










