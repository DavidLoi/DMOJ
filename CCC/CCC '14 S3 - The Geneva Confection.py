import sys

tests = int(sys.stdin.readline())

test = []
done = False

for i in range(tests):

    mountain = []
    lake = []
    branch = []

    numCars = int(sys.stdin.readline())

    for i in range(numCars):
        mountain.append(int(sys.stdin.readline()))

    while mountain:
        if len(branch) > 0 and branch[-1] == len(lake) + 1:
                lake.append(branch[-1])
                del branch[-1]
        elif mountain[-1] == len(lake) + 1:
            lake.append(mountain[-1])
            del mountain[-1]
        else:
            branch.append(mountain[-1])
            del mountain[-1]

    while branch and lake:
        if branch[-1] == len(lake) + 1:
            lake.append(branch[-1])
            del branch[-1]
        else:
            test.append("N")
            break

    done = True

    if len(lake) == numCars:
        test.append("Y")

for i in test:
    print(i)