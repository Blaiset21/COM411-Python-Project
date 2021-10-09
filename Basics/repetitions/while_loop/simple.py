# added the user input for how many cables should be removed
print("How many cables should I remove?")
# added the variables of the amount of cables there are and how many are removed
remove = int(input())
cables = 0
# added a while loop which will display the message removed cable until all cables are removed
while cables < remove:
    print("Removed cable.")
    cables = cables + 1
