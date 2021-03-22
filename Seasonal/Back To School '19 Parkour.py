x, y, h, v = [int(x) for x in input().split()]

t = int(input())

moves = 0

if x > 2 * y:
    y = int(x/2)
elif y > 2 * x:
    x = int(y/2)

sum = x + y

while sum % 3 != 0:
    sum += 1

moves += int(sum / 3)

if moves < t:
    print("YES")
else:
    print("NO")