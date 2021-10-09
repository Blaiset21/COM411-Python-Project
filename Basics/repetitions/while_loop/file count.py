# Added a line for user input as to how many cables should be avoided
print("How many live cables must I avoid?")
# added the variable for user input and a tracker variable
avoid = int(input())
live = 0
# added a while loop displaying the live cables avoided
while live < avoid:
    print("Avoiding...", end= "")
    live = live + 1
    print(f"...Done! {live} live cables avoided!")
# created a print statement at the end saying all the cables have been avoided
print("All live cables have been avoided.")
