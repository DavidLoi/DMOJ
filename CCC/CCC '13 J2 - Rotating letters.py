letters = ["I", "O", "S", "H", "Z", "X", "N"]

word = input()

count = 0

for i in word:
    if i in letters:
        count += 1
    else:
        count += 0

if count == len(word):
    print("YES")
else:
    print("NO")