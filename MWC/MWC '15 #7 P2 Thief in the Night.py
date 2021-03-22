import sys
input = sys.stdin.readline

f, r = input().split()

floors = []

for i in range(int(f)):
    floors.append(input().split())
    floors[i][0] = int(floors[i][0])

for i in floors:
    for n in range(int(r) - 1):
        i[n+1] = i[n] + int(i[n+1])

q = int(input())

for i in range(q):
    a, b, c = input().split()
    if int(a) == 1:
        print(floors[int(c)-1][int(b)-1])
    else:
        print(floors[int(c)-1][int(b)-1]-floors[int(c)-1][int(a)-2])