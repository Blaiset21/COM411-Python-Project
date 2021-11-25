def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences


def display_keys(data):
    print("Keys:")
    for key in data.keys():
        print(key)


def display_values(data):
    print("Values:")
    for value in data.values():
        print(value)


def display_items(data):
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    print("Dictionary:")
    display = pattern()
    print(display)
    display_keys(display)
    display_values(display)
    display_items(display)


run()