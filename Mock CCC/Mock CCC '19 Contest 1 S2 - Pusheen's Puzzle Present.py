size = int(input())

grid = []
good = 0
bad = 0

for i in range(size):
    grid.append([int(x) for x in input().split()])

for i in grid:
    for n in range(size - 1):
        if (i[n]) != (i[n + 1] - 1):
            bad += 1
            break

print(bad)