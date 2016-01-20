#!/bin/python3

def main():
    testfunc(one = 1, two = 2, four = 42)
    testfunc2(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)

def testfunc(**kwargs):
    print("In testfunc()")
    print(kwargs)  # args is a dictionary
    print("Displaying individual arguments")
    print(kwargs['one'], kwargs['two'], kwargs['four'])

def testfunc2(this, that, other, *args, **kwargs):
    print("In testfunc2()")
    print("Regular arguments:", this, that, other)
    print("Optional arguments as a tuple:", args)
    print("Keyword arguments:", kwargs['one'], kwargs['two'], kwargs['four'])

if __name__ == "__main__": main()
