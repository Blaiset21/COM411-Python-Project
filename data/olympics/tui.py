import csv

records = []
headings = []


def started(msg=""):
    print("----------------------------------------------------")
    print(f"Operation started: {msg}...\n")


def completed():
    print(""
          "Operation completed.")
    print("----------------------------------------------------")


def error(msg):
    print(f"Error! {msg}")


def menu():
    print(f"""Please select one of the following options:"
    {"[years]":<10}    List unique years
    {"[tally]":<10}    Tally up medals
    {"[team]":<10}   Tally up medals for each team
    {"[exit]":<10}     Exit the program""")
    selection = input("Your selection:")
    return selection


def display_medal_tally(tally):
    print(f"Gold:{tally['Gold']}")
    print(f"Silver:{tally['Silver']}")
    print(f"Bronze:{tally['Bronze']}")


def display_medal_tally(team_tally):
    for key, value in team_tally.items():
        print(f"{key}: {value}")


def display_years(years):
    sorted(years)
    print(years)


