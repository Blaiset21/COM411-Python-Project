def sum_weights(beep, bop):
    total_weight = bop + beep
    print(f"The sum of Beep and Bop's weight is {total_weight}.")


def calc_avg_weight(beep, bop):
    avg_weight1 = (beep + bop)/2
    print(f"The average of Beep and Bop's weight is {avg_weight1}.")


def run():
    print("What is the weight of Beep?")
    beep = int(input())
    print("What is the weight of Bop?")
    bop = int(input())
    print("What would you like to calculate (sum or average)?")
    sora = input()
    if sora == "average":
        calc_avg_weight(beep, bop)
    elif sora == "sum":
        sum_weights(beep, bop)


run()
