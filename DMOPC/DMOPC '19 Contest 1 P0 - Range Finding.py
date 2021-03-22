n = int(input())

nums = [int(x) for x in input().split()]

new = sorted(nums)

print(new[-1] - new[0])
