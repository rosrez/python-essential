#!/bin/python3

class Duck:
    # the constructor
    def __init__(self, number):
        self.number = number

    def quack(self):
        print("Quaaack! - My number is", self.number)

    def walk(self):
        print("Walks like a duck. My number is", self.number)

def main():
    donald = Duck(47)
    donald.quack()
    donald.walk()

    frank  = Duck(53)
    frank.quack()
    frank.walk()


if __name__ == "__main__": main()
