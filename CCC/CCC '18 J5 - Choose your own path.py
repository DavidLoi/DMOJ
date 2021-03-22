pages = int(input())

graph = [[0]]

for i in range(pages):
    add = input().split()
    add = [int(x) for x in add]
    graph.append(add)

queue = [1]
visited = []
count = 0
counter = 0
addCount = 1
length = 0
checkLen = True

while queue:

    current = queue[0]
    queue.pop(0)

    if count == counter and checkLen:
        length += 1
        count += addCount
        addCount = 0
        counter += 1

    else:
        counter += 1

    if graph[current] == [0]:
        checkLen = False

    if current not in visited:
        visited.append(current)
        for i in graph[current][1:]:
            queue.append(i)
            addCount += 1

if len(visited) == pages:
    print("Y")
else:
    print("N")

print(length)
