import sys
input = sys.stdin.readline

for i in range(5):
    currX = 50
    currY = 25
    x = int(input())
    y = int(input())

    while 0 < currX < 100 and 0 < currY < 50:
        currX += x
        currY += y

    print(str(currX) + "," + str(currY))