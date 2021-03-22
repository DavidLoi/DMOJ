num, children = [int(x) for x in input().split()]

orphanage = []
for i in range(num):
    orphanage.append([int(x) for x in input().split()])

for i in range(num):
    length = children
    for j in orphanage[i]:
        if j == 1 or j == 10:
            length -= 1
        orphanage[i] = length

most = 0
best = 1

for i in range(num):
    if orphanage[i] == children:
        best = i + 1
        break
    elif orphanage[i] > most:
        most = orphanage[i]
        best = i + 1

print(best)