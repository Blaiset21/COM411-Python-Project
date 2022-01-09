class Robot:
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    def the_laws():
        print(Robot.laws)

    def assemble(cls):
        return cls("Assembled Robot")

    def __init__(self, name="Robot"):
        self.name = name
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1

    def eat(self):
        if self.energy >= 90:
            pass
        else:
            self.energy += 10

    def move(self):
        if self.energy <= 10:
            pass
        else:
            self.energy -= 10

if __name__ == "__main__":
    robot = Robot()
    robot.display()
    print(repr(robot))
    print(robot)