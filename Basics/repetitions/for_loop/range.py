print("What level of brightness is required?")
bright = int(input())
print("Adjusting brightness...")
for count in range(2, bright+2, 2):
    print("Beep's brightness level: ", end="")
    print("*" * count)
    print("Bop's brightness level: ", end="")
    print("*" * count)
print("Adjustments complete!")