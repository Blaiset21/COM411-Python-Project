# added a section to allow the user to enter 3 numbers
print("Please enter the first whole number.")
first = int(input())
print("Please enter the second whole number.")
second = int(input())
print("Please enter the third whole number.")
third = int(input())
# added a 2 variables to check how many were odd/even
totalodd = int()
totaleven = int()
# added a set of if statements to check for each set of numbers being odd and even
if first % 2 != 0:
    totalodd = totalodd + 1
elif first % 2 == 0:
    totaleven = totaleven + 1
else:
    print("please enter a whole number")
if second % 2 != 0:
    totalodd = totalodd + 1
elif second % 2 == 0:
    totaleven = totaleven + 1
else:
    print("please enter a whole number")
if third % 2 != 0:
    totalodd = totalodd + 1
elif third % 2 == 0:
    totaleven = totaleven + 1
else:
    print("please enter a whole number")
if totalodd == 1:
    print("there were 2 even numbers and 1 odd number")
elif totalodd == 2:
    print("there was 1 even number and 2 odd numbers")
elif totalodd == 3:
    print("there was 0 even numbers and 3 odd numbers")
elif totalodd == 0:
    print("there were 3 even numbers and 0 odd numbers")


