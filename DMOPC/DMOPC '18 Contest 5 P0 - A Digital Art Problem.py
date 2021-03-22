operation = input()
r = []
g = []
b = []

for i in range(2):
    x, y, z = [float(x) for x in input().split()]
    r.append(x)
    g.append(y)
    b.append(z)

if operation == "Multiply":
    red = r[0] * r[1]
    green = g[0] * g[1]
    blue = b[0] * b[1]

    print(red, green, blue)

elif operation == "Screen":
    red = 1 - (1 - r[0]) * (1 - r[1])
    green = 1- (1 - g[0]) * (1 - g[1])
    blue =  1- (1 - b[0]) * (1 - b[1])

    print(red, green, blue)

elif operation == "Overlay":
    if r[0] < 0.5:
        red = (2 * r[0] * r[1])
    else:
        red = (1 - 2 * (1 - r[0]) * (1 - r[1]))
    if g[0] < 0.5:
        green = (2 * g[0] * g[1])
    else:
        green = (1 - 2 * (1 - g[0]) * (1 - g[1]))
    if b[0] < 0.5:
        blue = (2 * b[0] * b[1])
    else:
        blue = (1 - 2 * (1 - b[0]) * (1 - b[1]))

    print(red, green, blue)
