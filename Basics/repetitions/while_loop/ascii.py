# added in a print statement for user input as for how many bars should be charged
print("How many bars should be charged?")
# added a counting variable and a total variable
charge = int(input())
battery = 0
# added a while loop to display asci art
while battery < charge:
    print("Charging:", end= "")
    battery = battery + 1
    print("█ " * battery)
print("The battery is fully charged.")