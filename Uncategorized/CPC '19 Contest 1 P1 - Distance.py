num = int(input())

path = []

if num%2 == 0:
    for i in range((int(num/2))):
        path.append(i+1)
        path.append(num-i)

elif num % 2 == 1:
    for i in range(int((num-1)/2)):
        path.append(i+1)
        path.append(num-i)
    path.append(int(num/2) + 1)

print(" ".join(str(x) for x in path))