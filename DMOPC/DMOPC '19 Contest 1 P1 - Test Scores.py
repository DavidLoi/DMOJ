tests = int(input())

for i in range(tests):
    n, a, b, t = [int(x) for x in input().split()]

    total = 0
    sum = a + b
    q = 0

    total = a * n

    room = (total - t) // sum

    if room == -1:
        print(room)
    else:
        print(n - room)