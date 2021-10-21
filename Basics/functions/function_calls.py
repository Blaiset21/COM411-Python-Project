def box(word):
    square = int(len(word)+4)
    print("-"*square)
    print(f"- {word} -")
    print("-"*square)


def lower_case(word):
    print(word.lower())


def upper_case(word):
    print(word.upper())


def mirrored(word):
    revstr = []
    reverse_word = len(word)
    while reverse_word > 0:
        revstr += word[reverse_word - 1]
        reverse_word = reverse_word - 1
    print(revstr)


def repeat(word):
    print("how many times would you like the word to be repeated?")
    num = int(input())
    count = 1
    while count <= num:
        if (count % 2) == 0:
            print(word.upper())
            count = count + 1
        else:
            print(word.lower())
            count = count + 1


print("Enter a word")
word = input()
print("choose one of the following: Display in a Box, Display a word in Lower case,"
      " Display a word in Upper case, Display a word Mirrored or Repeat a word")
choice = input()
if choice == "Display in a Box" or choice == "display in a box":
    box(word)
elif choice == "Display a word in Lower case" or choice == "display a word in lower case":
    lower_case(word)
elif choice == "Display a word in Upper case" or choice == "display a word in upper case":
    upper_case(word)
elif choice == " Display a word Mirrored" or choice == "display a word mirrored":
    mirrored(word)
elif choice == "Repeat a word" or choice == "repeat a word":
    repeat(word)