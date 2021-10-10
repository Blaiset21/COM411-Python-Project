print("What phrase do you see?")
word = input()
print("Reversing...")
print("The phrase is ", end="")
backwards = ""
for letter in word:
    backwards = letter + backwards
print(backwards)