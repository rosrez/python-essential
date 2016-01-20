#!/bin/python3

class Duck:
    # note the absense of the constructor
    # Python seems to provide a default constructor

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("Walks like a duck")

def main():
    # this calls the constructor to create an instance of class Duck
    donald = Duck()
    # see what donald is
    print("donald is:")
    print(donald)
    print("donald's ID is", id(donald))

    # method invocations
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
