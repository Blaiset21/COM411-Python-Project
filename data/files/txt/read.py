def display_chars (path,char):
    with open(path) as file:
        data = file.read(char)
        print("The first 5 characters are:")
        print(data)


def display_line(path):
    with open(path) as file:
        data = file.readline().strip()
        print("The first line is:")
        print(data)


def display_text(path):
    with open(path) as file:
        data = file.read()
        print("The full text is:")
        print(data)


def run():
    display_chars("library.txt",5)
    display_line("library.txt")
    display_text("library.txt")


if __name__ == "__main__":
    run()