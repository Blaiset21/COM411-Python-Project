def box(word):
    square = int(len(word)+4)
    print("-"*square)
    print(f"- {word} -")
    print("-"*square)


def lower_case(word):
    print(word.lower())


def upper_case(word):
    print(word.upper())


print("Enter a word")
word = input()
print("choose one of the following: Display in a Box, Display a word in Lower case,"
      " Display a word in Upper case, Display a word Mirrored Repeat a word")
choice = input()
if choice == "Display in a Box" or choice == "display in a box":
    box(word)
elif choice == "Display a word in Lower case" or choice == "display a word in lower case":
    lower_case(word)