#!/bin/python3

# print a Fibonacci series (less than 50)

a, b = 0, 1

while b < 50:
    print(b)
    a, b = b, a + b
print("Done.")      # NOT INDENTED, i.e. NOT PART OF THE LOOP! 
