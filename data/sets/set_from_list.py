def observed():
    observations = []
    for count in range(7):
        print("Please enter an observation:")
        observe = input()
        observations.append(observe)
    return observations


def run():
    print("Counting observations...")
    store = observed()
    see = set()
    for observation in store:
      data = (observation, store.count(observation))
      see.add(data)

    for data in see:
        print(f"{data[0]} observed {data[1]} times")


run()