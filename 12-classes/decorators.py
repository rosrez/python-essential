#!/bin/python3

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("Walks like a duck.")

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    # The following set of accessor functions with @ modifiers
    # enables us to use color as an object property, i.e.
    # we can get the value by using c = color, set it using
    # color = c.

    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    print("'Raw' access to fields")
    donald = Duck(color = "white")
    print("My color is", donald.get_property("color"))

    print("Access using decorators")
    frank = Duck()
    frank.color = "blue"
    print("My color is", frank.color)

if __name__ == "__main__": main()
