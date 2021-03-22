import sys

n = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]

nums.sort()
min = nums[1] - nums[0]
for i in range(len(nums) - 1):
    temp = nums[i + 1] - nums[i]
    if temp < min:
        min = temp
print(min)