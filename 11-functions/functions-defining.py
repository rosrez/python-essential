#!/bin/python3

def main():
    testfunc(42)
    testfunc(42, 16)
    testfunc(42, 16, 36)
    testfunc2(42)
    testfunc2(42, 16)
    testfunc3(42)
    testfunc3(42, 16)

def testfunc(number, another = 43, onemore = 75):
    print('This is a test function:', number, another, onemore)

def testfunc2(number, another = None, onemore = 75):
    print('This is test function 2:', number, another, onemore)

def testfunc3(number, another = None, onemore = 75):
    if another is None:
        another = 112
    print('This is test function 3:', number, another, onemore)

def stubfunc():
    # the pass statement is a no-op 
    # that prevents interpreter errors 
    # since it's a syntax error to have a function without a body
    pass

# This pattern at the end of the file so that main() 
# can call functions defined in arbitrary order.
if __name__ == "__main__": main()
