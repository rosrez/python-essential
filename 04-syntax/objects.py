#!/bin/python3

class Egg:
    # the first parameter refers to the object, can be named differently 
    # though self is
    def __init__(self, kind = "fried"):     
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg();
    scrambled = Egg("scrambled")
    print(fried.whatKind())
    print(scrambled.whatKind())

if __name__ == "__main__": main()
