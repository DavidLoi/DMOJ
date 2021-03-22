shoes = input().split()

nums = [1,2,3,4]
s1 = 0
s2 = 0

for i in range(len(shoes)):
    if shoes[i] == "L":
        s1 = i + 1
    elif shoes[i] == "R":
        s2 = i + 1

nums.remove(s1)
nums.remove(s2)

print(s1, s2)
print(nums[0],nums[1])