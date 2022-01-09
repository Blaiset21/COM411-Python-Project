class Human:
    MAX_ENERGY = 100

    def __init__(self,  name="Human", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'human {self.name} is {self.age} years old.'

    def grow(self):
        self.age += 1

    def eat(self):
        if self.energy >= 80:
            pass
        else:
            self.energy += 20

    def move(self):
        if self.energy <= 20:
            pass
        else:
            self.energy -= 20

if __name__ == "__main__":
    human = Human()
    human.display()
    print(repr(human))
    print(human)
