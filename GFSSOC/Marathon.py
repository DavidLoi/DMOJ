import sys
input = sys.stdin.readline

n, q = [int(x) for x in input().split()]

ratings = [int(x) for x in input().split()]

prefix = [0]

for i in range(n):
    prefix.append(ratings[i] + prefix[i])

for i in range(q):
    a, b = [int(x) for x in input().split()]
    print(prefix[-1] - prefix[b] + prefix[a - 1])