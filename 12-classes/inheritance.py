#!/bin/python3

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walking here!')
    def clothes(self): print('I have nice clothes')

# this illustrates the inheritance syntax

class Duck(Animal):
    def quack(self):
        print("Quaaack!")

    # overrides walk() in Animal
    def walk(self):
        # super() accesses the ancestor class
        # note that the invocation is super(), not self.super() !
        super().walk()
        print("Walks like a duck")

class Dog(Animal):
    def clothes(self):
        print("I have brown and white fur")

def main():
    print("Duck")
    donald = Duck()
    
    # method invocations
    donald.quack()

    # This prints:
    #   Hey! Im walking here!
    #   Walks like a duck
    #
    # because we call super().walk() in Duck.walk() 
    # and then print a string that's unique string.
    donald.walk()
   
    print("Dog")
    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()
