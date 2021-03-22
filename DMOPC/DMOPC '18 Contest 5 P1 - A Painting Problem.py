n, m, k = [int(x) for x in input().split()]

n = "0000000000000000000000000000000000000000000000000" + bin(n)[2:]
m = "0000000000000000000000000000000000000000000000000" + bin(m)[2:]

blue = 0
purple = 0

for i in range(1, k + 1):
    if n[-i] == "1" and m[-i] != "1":
        blue += 1

    elif n[-i] != "1" and m[-i] == "1":
        blue += 1

    else:
        purple += 1

print(blue, purple)