def cross_bridge(steps):
    count = 0
    while steps > count:
        print("Crossed step")
        count = count + 1
    if count > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going!")
cross_bridge(3)
cross_bridge(6)
