colors = int(input())
pink = 0

for i in range(colors):
    r, g, b = [int(x) for x in input().split()]
    if r >= 240 and r <= 255:
        if g >= 0 and g <= 200:
            if b >= 95 and b <= 220:
                pink += 1

print(pink)