class Planet:

    def __init__(self, human=[], robot=[]):
        self.human = human
        self.robot = robot

    def __repr__(self):
        return f"planet(humans={self.human}, robots={self.robot})"

    def __str__(self):
        return f"This planet has {len(self.human)} humans and {len(self.robot)} robots."

    def add_human(self):
        self.human.append("human")

    def add_robot(self):
        self.robot.append("robot")

    def remove_human(self):
        self.human.append("human")

    def remove_robot(self):
        self.robot.append("robot")


if __name__ == "__main__":
    planet = Planet()
    print(planet)
    print(repr(planet))
