year = int(input())

done = False

def distinct(n):
    n = str(n)
    nums = []
    for i in n:
        nums.append(int(i))
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return False
    else:
        return True

while not done:
    year += 1
    if distinct(year) == True:
        done = True

print(year)