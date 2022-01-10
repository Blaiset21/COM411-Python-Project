from human import Human
from robot import Robot
class Planet:

    def __init__(self):
        self.inhabitants = []

    def __repr__(self):
        return f"planet(inhabitants={self.inhabitants})"

    def __str__(self):
        return f"This planet has {len(self.inhabitants)} inhabitants"

    def add(self, inhabitant):
        self.inhabitants.append(inhabitant)

    def remove(self, inhabitant):
        self.inhabitantsappend(inhabitant)


if __name__ == "__main__":
    planet = Planet()
    print(repr(planet))
    blaise = Human("blaise")
    planet.add(blaise)
    robot = Robot("Robot")
    planet.add(robot)
    print(repr(planet))
    print(planet)