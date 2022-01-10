from inhabitant import Inhabitant


class Human(Inhabitant):
    MAX_ENERGY = 100

    def __init__(self,  name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'human {self.name} is {self.age} years old and my energy is {self.energy}.'


if __name__ == "__main__":
    human = Human()
    print(repr(human))
    human.move(10)
    print(repr(human))
    human.eat(5)
    print(repr(human))
    human.eat(20)
    print(repr(human))