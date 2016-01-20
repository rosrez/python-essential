#!/bin/python3

# We define the inclusive_range() generator function that mimics the regular range() function
# except that the range it returns is inclusive.
# We call the function in three different ways to check the effect of each optional argument.

def main():
    print("inclusive_range(25)")
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

    print("inclusive_range(5,25)")
    for i in inclusive_range(5, 25):
        print(i, end = ' ')
    print()

    print("inclusive_range(5, 25, 3)")
    for i in inclusive_range(5, 25, 3):
        print(i, end = ' ')
    print()

# We cannot define inclusive_range like this:
#
# def inclusive_range(start = 0, stop, step = 1)
#
# The reason is that all required arguments (such as 'stop' in this case)
# must appear before optional arguments (the ones that have default values)

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        # note the asssignment to multiple variables from a tuple
        (start, stop) = args
        step = 1
    elif numargs == 3:
        # note the assignment to multiple variables from a tuple
        (start, stop, step) = args
    else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        # yield returns a value, just as return does
        # The only difference is that when the function is called again, it picks up where it left off.
        # This allows us to build iterator functions in Python.
        yield i
        i += step

if __name__ == "__main__": main()
