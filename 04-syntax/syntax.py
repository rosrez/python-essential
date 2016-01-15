#!/usr/bin/python3

def main():
    print("This is the syntax.py")
    # we can call the egg function (which is defined below) because we have included the line at the bottom of the file
    egg()       

def egg():
    print("egg")

# It is a very common practice in Python to include this line.
# This allows us to call function regardless if they are defined at the point when whe call them.
# This also invokes the main() function only if the module is run as the main module. 
# If the module is invoked by another module (say, by calling a function), the main() function does not get called.
# This construnct is very useful for unit testing; tests fire only if the module is called by itself.
if __name__ == "__main__": main()
