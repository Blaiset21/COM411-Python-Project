print("What user_word do you see?")
user_word = input()
print("Reversing...")
print("The user_word is: ", end="")
for count in range(len(user_word)-1, -1, -1):
    print(user_word[count], end="")
