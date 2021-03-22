n = int(input())

t = int(input())

cups = -1
total = 0

while total < n:
    cups += 1
    total = (2**cups)**t

print(cups)