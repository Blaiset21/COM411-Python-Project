print("Program Started!")
print("Please enter a standard character:")
char = input()
if len(char) == 1:
    value = ord(char)
    print(f"The ASCII code for {char} is: {value}")
else:
    print("Please enter a standard character:")
print("Program Ended!")