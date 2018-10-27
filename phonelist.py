cases = int(input())

def checker(nums):
	numsL = len(nums)
	for i in range(0, numsL-1):
		if(len(nums[i]) <= len(nums[i+1]) and nums[i] == nums[i+1][:len(nums[i])]):
			return True
	return False

for _ in range(cases):
	numnum = int(input())
	nums = []
	for _ in range(numnum):
		nums.append(input())
	if(checker(sorted(nums)) == True):
		print("NO")
	else:
		print("YES")