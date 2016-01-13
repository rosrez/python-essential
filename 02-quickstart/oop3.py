#!/bin/python3

# -- VIEW --

class AnimalActions:
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()

# -- MODEL --

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaack!",
        feathers = "The duck has gray and white feathers."
    )

class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

# -- CONTROLLER --

def in_the_doghouse(dog):
    print(dog.bark())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for o in (donald, john, fido):
        in_the_forest(o)

    print("- In the doghouse:")
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__": main()
