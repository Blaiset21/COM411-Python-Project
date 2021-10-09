print("How many numbers should I sum up?")
numbers = int(input())
count = 1
total = 0
while count <= numbers:
    print(f"Please enter number {count} of {numbers}:")
    usern = int(input())
    total = total + usern
    count = count + 1
print(f"The answer is {total}")
