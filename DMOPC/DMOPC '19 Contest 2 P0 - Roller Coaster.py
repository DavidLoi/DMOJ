n, min, max = [int(x) for x in input().split()]

children = [int(x) for x in input().split()]

children.sort()
count = 0

for i in children:
	if i >= min and i <= max:
		count += 1

print(count)