def observed():
    observations = []
    for count in range(5):
        print("Please enter an observation:")
        observe = input()
        observations.append(observe)
    return observations


def remove_observations(observations):
    is_running = True
    while(is_running):
        print("Do you wish to remove an observation (yes/no)?")
        yn = input()
        if yn == "yes":
            print("What observation do you wish to remove?")
            gone = input()
            observations.remove(gone)
        else:
            is_running = False


def run():
    print("Counting observations...")
    store = observed()
    remove_observations(store)
    see = set()
    for observation in store:
        data = (observation, store.count(observation))
        see.add(data)

    for data in see:
        print(f"{data[0]} observed {data[1]} times")


run()