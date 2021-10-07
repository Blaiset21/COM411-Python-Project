# added a nested loop for the user
print("What type of cover does the book have?")
cover = input()
if cover == "soft":
    print("Is the book perfect-bound?")
    book = input()
    if book == "yes":
        print("Soft cover, perfect bound books are very popular!")
    elif book == "no":
        print("Soft covers with coils or stitches are great for short books")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")