import sys
input = sys.stdin.readline

n = int(input())
numCards = [int(x) for x in input().split()]
valueCards = [int(x) for x in input().split()]

currValue = 0
totalValues = []

for i in range(n):
    currValue += numCards[i] * valueCards[i]

totalValues.append(currValue)

currValue = 0

n = int(input())
numCards = [int(x) for x in input().split()]
valueCards = [int(x) for x in input().split()]

for i in range(n):
    currValue += numCards[i] * valueCards[i]

totalValues.append(currValue)

print(str(totalValues[0]) + " " + str(totalValues[1]))