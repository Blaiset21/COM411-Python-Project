print("Program Started!")
print("Please enter an ASCII code:")
ASCII = input()
num = int(ASCII)
if num in range(32,126):
    value = chr(num)
    print(f"The character represented by the ASCII code {ASCII} is {value}")
else:
    print("Please enter an ASCII code:")
print("Program Ended!")
