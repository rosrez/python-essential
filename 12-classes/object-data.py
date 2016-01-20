#!/bin/python3

class Duck:
    # the constructor
    def __init__(self, color = 'white'):
        self._color = color

    def quack(self):
        print("Quaaack! - My number is", self.number)

    def walk(self):
        print("Walks like a duck. My number is", self.number)

    # accessor methods are just normal methods

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    donald = Duck()
    print(donald.get_color())
    donald.set_color('blue')
    print(donald.get_color())

    # In Python, we can access the object field directly!
    print(donald._color)

if __name__ == "__main__": main()
