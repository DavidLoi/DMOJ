import sys

questions = int(sys.stdin.readline())

reply = []
answer = []
correct = 0

for i in range(questions):
    reply.append(sys.stdin.readline())

for i in range(questions):
    answer.append(sys.stdin.readline())

for i in range(questions):
    if reply[i] == answer[i]:
        correct += 1

print(correct)