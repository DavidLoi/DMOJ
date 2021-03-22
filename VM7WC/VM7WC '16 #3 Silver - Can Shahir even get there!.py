numHouses, numRoads, start, end = [int(x) for x in input().split()]

connections = [[] for n in range(numHouses + 1)]
connections[0].append("*")

for i in range(numRoads):
    x, y = input().split()
    connections[int(x)].append(int(y))
    connections[int(y)].append(int(x))

def path(current, end):
    visited = []
    queue = [[start]]

    while queue:
        check = queue.pop(0)

        if end in check:
            return True

        else:
            for i in check:
                if i not in visited:
                    visited.append(i)
                    queue.append(connections[i])

if path(start, end):
    print ("GO SHAHIR!")
else:
    print("NO SHAHIR!")