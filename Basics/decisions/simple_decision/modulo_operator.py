# asks the user to enter a whole number
print("Please enter a whole number")
numbers = int(input())
if numbers % 2 != 0:
    print(f"The number {numbers} is an odd number")
elif numbers % 2 == 0:
    print(f"The number {numbers} is an even number")
else:
    print("please enter a whole number")
