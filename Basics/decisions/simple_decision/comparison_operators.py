# added a comparsion if statement
print("Please enter the first number.")
first = int(input())
print("Please enter the second number.")
second = int(input())
if first < second:
    print("the First is the smallest")
elif first > second:
    print("the Second is the smallest")
elif first == second:
    print("Both are equal")
