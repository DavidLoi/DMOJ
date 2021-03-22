numMarkers = int(input())

markerList = input().split(" ")

length = 0

red = 0
orange = 0
yellow = 0
green = 0
blue = 0
black = 0

for i in markerList:
    if i == "red":
        red += 1
    elif i == "orange":
        orange += 1
    elif i == "yellow":
        yellow += 1
    elif i == "green":
        green += 1
    elif i == "blue":
        blue += 1
    elif i == "black":
        black += 1

colors = [red, orange, yellow, green, blue, black]

colors.sort(reverse=True)

while len(colors) > 0:
    if colors[0] > 0:
        colors[0] -= 1
        length += 1
        if len(colors) > 1:
            if colors[1] > 0:
                colors[1] -= 1
                length += 1
            else:
                colors.pop(1)
                if len(colors) > 1:
                    if colors[1] > 0:
                        colors[1] -= 1
                        length += 1
                    else:
                        colors = []
                else:
                    colors = []
        else:
            colors = []
    else:
        colors.pop(0)

print(length)