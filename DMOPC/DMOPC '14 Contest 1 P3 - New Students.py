numOld = int(input())

oldTotal = 0

for student in range(numOld):
    oldTotal += int(input())

numNew = int(input())

for student in range(numNew):
    oldTotal += int(input())
    numOld += 1
    avg = round(oldTotal / numOld, 3)
    print(avg)