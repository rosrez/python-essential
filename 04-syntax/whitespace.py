#!/usr/bin/python3

def main():
    print("This is the syntax.py")  # indented - tells Python that it's the body of the main() function
    # if we indent this line differently (e.g. by 1, 2 or 3 spaces), Python will display a syntax error
    print("This is another line.")
    space()
# This line doesn't belong to main() because it is not indented.
print("This gets printed before the output main()")

# A construct where a function consists of a single statement combined with the function definition/name:

def space(): print("Another function")
#           ^ - This space is insignificant, it can be removed altogether or there may be more spaces

if __name__ == "__main__": main()
