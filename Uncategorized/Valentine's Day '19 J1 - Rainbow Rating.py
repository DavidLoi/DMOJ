users = int(input())
list = []

for i in range(users):
    current = int(input())
    if current < 1000:
        list.append("Newbie")
    elif current < 1200:
        list.append("Amateur")
    elif current < 1500:
        list.append("Expert")
    elif current < 1800:
        list.append("Candidate Master")
    elif current < 2200:
        list.append("Master")
    elif current < 3000:
        list.append("Grandmaster")
    elif current < 4000:
        list.append("Target")
    else:
        list.append("Rainbow Master")

for i in list:
    print(i)