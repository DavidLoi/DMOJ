n = int(input())

mid = n // 2
quarter = mid // 2

nums = [int(x) for x in input().split()]

nums.sort()

min = nums[0]
max = nums[-1]

if n % 2 == 0:
    q2 = (nums[mid - 1] + nums[mid])/2
    if mid % 2 == 0:
        q1 = (nums[quarter - 1] + nums[quarter]) / 2
        q3 = (nums[mid + quarter - 1] + nums[mid + quarter]) / 2
    else:
        q1 = nums[quarter]
        q3 = nums[mid + quarter]
else:
    q2 = nums[mid]
    if mid % 2 == 0:
        q1 = (nums[quarter - 1] + nums[quarter])/2
        q3 = (nums[mid + quarter] + nums[mid + quarter + 1])/2
    else:
        q1 = nums[quarter]
        q3 = nums[mid + quarter + 1]

print(min, max, q1, q2, q3)