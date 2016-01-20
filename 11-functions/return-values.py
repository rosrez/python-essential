#!/bin/python3

def main():
    # this prints the result value of testfunc(), which is a string
    print(testfunc())
    # this prints range(0, 25) because range() returns a range object
    print(range(25))
    # we can use the range object returned by rangefunc() as an iterator
    for n in rangefunc(): print(n, end=' ')
    print()

def testfunc():
    return 'This is a test function'

def rangefunc():
    return range(25)

if __name__ == "__main__": main()
