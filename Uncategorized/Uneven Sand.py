import sys
input = sys.stdin.readline

l = int(1)
r = int(2000000000)
state = " "
count = 1

while state != "OK\n":
    mid = int((l + r)//2)
    print(mid)
    sys.stdout.flush()
    state = input()
    if state == "FLOATS\n":
        r = mid - 1
    elif state == "SINKS\n":
        l = mid + 1

sys.exit()