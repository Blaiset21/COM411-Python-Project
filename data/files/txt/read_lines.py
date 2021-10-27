def search(file_name):
    print("searching...")
    with open(file_name) as file:
        for line in file:
            print(f"Looked in {line.strip()}")
        print("done")


def run():
    search("library.txt")


if __name__ == "__main__":
    run()