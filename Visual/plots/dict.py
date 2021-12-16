import matplotlib.pyplot as plt


def data():
    paths = {}
    print("What type of line would you like? : for dotted, - for solid or -- for dashed")
    line = input()
    print("what type of colour would you like? r for red, g for green or b for blue")
    colour = input()
    print("what type of style would you like? o,s or ^")
    style = input()
    paths['line'] = line
    paths['colour'] = colour
    paths['style'] = style
    return paths


def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())
    for num_lines in range(num_lines):
        values = data()
        import random
        x = random.sample(range(1, 10),5)
        y = random.sample(range(1,10),5)
        format = f"{values['colour']}{values['line']}{values['style']}"
        plt.plot(x,y,format)
        plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")

run()