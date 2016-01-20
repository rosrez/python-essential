#!/bin/python3

# This script illustrates generator classes.
# We define our own range class to mimic Python's range class, 
# except that our range is inclusive.

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))

    # The special 'iterator' method which makes 
    # this class's objects iterator objects.
    # 
    # Whenever a caller iterates through the object (like in a for-loop),
    # the __iter__() method gets called automatically.
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    print("Regular range -- range(25)")
    o = range(25)
    for i in o: print(i, end = ' ')
    print()

    print("Inclusive range -- inclusive_range(25)")
    o = inclusive_range(25)
    for i in o: print(i, end = ' ')
    print()

    print("Inclusive range -- inclusive_range(5,25)")
    o = inclusive_range(5, 25)
    for i in o: print(i, end = ' ')
    print()

    print("Inclusive range -- inclusive_range(5,25,2)")
    o = inclusive_range(5, 25, 2)
    for i in o: print(i, end = ' ')
    print()

if __name__ == "__main__": main()
