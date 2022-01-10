import matplotlib.pyplot as plt
import random


def data():
    paths = {}
    print("What type of line would you like:\n"
          "[:] Dotted\n"
          "[--] Dashed\n"
          "[-] Straight")
    line_type = input()
    print("What colour would you like:\n"
          "[r] red\n"
          "[g] greed\n"
          "[b] blue")
    colour = input()
    print("What type of Marker would you like:\n"
          "[o] Circle\n"
          "[s] Square\n"
          "[^] Up arrow")
    marker_type = input()
    paths['line_type'] = line_type
    paths['colour'] = colour
    paths['marker_type'] = marker_type
    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for count in range(lines):
        values = data()
        x = random.sample(range(1, 10), 5)
        y = random.sample(range(1, 10), 5)
        formatting = f"{values['colour']}{values['line_type']}{values['marker_type']}"
        plt.plot(x, y, formatting)
    plt.show()


def run():
    print("Running....")
    generate()
    print("Done!")


run()
