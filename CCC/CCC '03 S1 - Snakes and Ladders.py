import sys
input = sys.stdin.readline

curr = 1
game = True

while game:
    die = int(input())
    if curr + die <= 100:
        curr += die

    if curr == 54:
        curr = 19
    elif curr == 90:
        curr = 48
    elif curr == 99:
        curr = 77
    elif curr == 9:
        curr = 34
    elif curr == 40:
        curr = 64
    elif curr == 67:
        curr = 86

    if curr == 100:
        print("You are now on square 100")
        print("You Win!")
        game = False
    elif die == 0:
        print("You Quit!")
        game = False
    else:
        print("You are now on square " + str(curr))
