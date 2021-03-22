import sys
input = sys.stdin.readline

q = int(input())
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
speed = 0

if q == 1:
    a.sort()
    b.sort()
    for i in range(n):
        speed += max(a[i],b[i])

elif q == 2:
    a.sort()
    b.sort(reverse=True)
    for i in range(n):
        speed += max(a[i],b[i])

print(speed)