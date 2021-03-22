numTests = int(input())

total = 0

for i in range(numTests):
    score = int(input())
    total += score

print(total/numTests)