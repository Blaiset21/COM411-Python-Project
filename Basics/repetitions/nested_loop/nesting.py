print("Please enter a sequence of characters consisting of dashes and two markers")
user_spot = input()
print("Please enter the character for the marker")
marker = input()
distance = -1
distance2 = -1
for count in range(0,len(user_spot),1):
    letter = user_spot[count]
    if marker == letter:
        if (distance == -1):
            distance = count
        else:
            distance2 = count
    else:
        distance = distance
print(f"The distance between the markers is {distance2 - distance - 1}.")

