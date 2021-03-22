from sys import stdin, stdout

numTrees = int(stdin.readline())

weight = []

for i in range(numTrees):
    weight.append(int(stdin.readline()))

sumWeight = weight

sumWeight[0] = weight[0]

for i in range(1, len(weight)):
    sumWeight[i] = sumWeight[i - 1] + weight[i]

queries = int(stdin.readline())

for i in range(queries):
    a, b = stdin.readline().split()
    if a == "0":
        total = sumWeight[int(b)]
    else:
        total = sumWeight[int(b)] - sumWeight[int(a) - 1]
    print(total)