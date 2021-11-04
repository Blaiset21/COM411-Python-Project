def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    list = directions()
    for index in range(len(list)):
        print(f"{index}: {list[index]}")
    index = int(input())
    return list[index]


def run():
    route = []
    print("Working out escape route...")
    for count in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()