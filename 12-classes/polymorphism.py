#!/bin/python3

class Duck:
    # note the absense of the constructor
    # Python seems to provide a default constructor

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("Walks like a duck")

    def bark(self):
        print("Duck cannot bark")

    def fur(self):
        print("The duck has feathers")

class Dog:
    def bark(self):
        print("Woof!")

    def fur(self):
        print("The dog has brown and white fur")

    def walk(self):
        print("Walks like a dog")

    def quack(self):
        print("The dog cannot quack")

# we can pass Duck objects to in_the_forest() and Dog objects to in_the_pond()
# because they implement the interfaces that these functions expect.

# OK to pass a Duck object here since our Duck implements bark() and fur()
def in_the_forest(animal):
    animal.bark()
    animal.fur()

# OK to pass a Dog object here since our Dog implements quack() and walk()
def in_the_pond(duck):
    animal.quack()
    animal.walk()

def main():
    donald = Duck()
    fido = Dog()

    # using the objects regardless of the class
    for o in (donald, fido):
        in_the_pond(o)
        in_the_forest(o)

if __name__ == "__main__": main()
