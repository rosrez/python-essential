#!/bin/python3

class Duck:
    # the constructor that takes keyword arguments
    def __init__(self, **kwargs):
        # We employ kwargs.get() instead of kwargs[] because
        # the latter will give us an error if there is no such key in the dictionary.
        self._color = kwargs.get('color', 'white')

    def quack(self):
        print("Quaaack! - My number is", self.number)

    def walk(self):
        print("Walks like a duck. My number is", self.number)

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    donald = Duck()
    # will print the 'default color', which is white
    print(donald.get_color())

    frank = Duck(color = 'blue')
    # will print 'blue'
    print(frank.get_color())
if __name__ == "__main__": main()
