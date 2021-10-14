def display_ladder(steps):
    count = 0
    while count < steps:
        print("|    |")
        print("******")
        print("|    |")
        count = count + 1


def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)


create_ladder()
