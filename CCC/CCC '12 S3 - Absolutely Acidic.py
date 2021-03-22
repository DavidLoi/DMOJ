readings = [0 for i in range(1000)]

num = int(input())

for i in range(num):
    n = int(input())
    readings[-n] += 1


frequency = sorted(readings, reverse=True)

a = frequency[0]
b = frequency[1]

x = [index for index, value in enumerate(readings) if value == a]
y = [index for index, value in enumerate(readings) if value == b]

best = 0

if x == y:
    print(x[-1] - x[0])
else:
    best = x[-1] - y[0]
    m = y[-1] - x[0]
    if m > best:
        print(m)
    else:
        print(best)