n = int(input())

list = input().split()

word = input()

list.sort()

replace = ""
min = 100

for i in list:
    if len(i) == len(word):
        replace = i
        break
    else:
        curr = len(word) - len(i)
        if 0 < curr < min:
            min = curr
            replace = i

print(replace)