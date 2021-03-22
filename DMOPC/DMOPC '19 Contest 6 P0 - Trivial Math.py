import sys
input = sys.stdin.readline

lengths = [int(x) for x in input().split()]

lengths.sort(reverse=True)

if lengths[0] >= lengths[1] + lengths[2]:
    print("no")
else:
    print("yes")