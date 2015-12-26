#!/bin/python3

a, b = 0, 1     # note the multiple assignment syntax

# note that the "string".format() is a method of a string class

if a < b:   # colon followed by the code that is indented (this is called suite in python)
    print('a ({}) is less than b ({})'.format(a, b))    # {} is replaced with values of a and b, respectively
else:       # colon followed by another indented block of code
    print('a ({}) is not less than b ({})'.format(a, b))

# conditional expression (resemples C, but with a different syntax)
print("a is less than b" if a < b else "a is not less than b")
