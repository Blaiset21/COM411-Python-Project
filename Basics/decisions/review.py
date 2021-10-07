print("please enter a number between 1 and 10")
number = int(input())
print("now please enter the letter a, b or c")
letter = input()
if (letter == "a") and (number >= 5):
    print("please the letter d, f or g")
    letter2 = input()
    if letter2 == "d":
        print(f"{number}{letter}{letter2}")
    elif letter2 == "f":
        print(f"{number}{letter}{letter2}")
    elif letter2 == "g":
        print(f"{number}{letter}{letter2}")
    else:
        print("please the letter d, f or g")
elif (letter == "a") or (number >= 5):
    print("please the letter h, i or j")
    letter2 = input()
    if letter2 == "h":
        print(f"{number}{letter}{letter2}")
    elif letter2 == "i":
        print(f"{number}{letter}{letter2}")
    elif letter2 == "j":
        print(f"{number}{letter}{letter2}")
    else:
        print("please the letter h, i or j")
