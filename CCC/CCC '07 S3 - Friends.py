students = int(input())

friends = []
xlist = []
ylist = []

for i in range(students):
    x, y = input().split()
    xlist.append(int(x))
    ylist.append(int(y))

num = sorted(xlist)

friendship = [0 for x in range(num[-1] + 1)]

friendship[0] = '*'

for i in range(len(xlist)):
    friendship[xlist[i]] = ylist[i]

def bfs(friendship, start, end):
    distance = -1
    visited = []
    queue = [start]
    while queue:
        for i in queue:
            if i == end:
                return"Yes " + str(distance)
            elif i in visited:
                return("No")
            else:
                queue.append(friendship[i])
                visited.append(i)
                distance += 1

done = False
while not done:
    start, end = input().split()
    if int(start) + int(end) == 0:
        done = True
    else:
        print(bfs(friendship, int(start), int(end)))
