#!/usr/bin/python3

def main():
    a = 1
    s = "one"
    print(type(a), a) # everything in Python is a class, so this produces the following output: <class 'int'> 1
    print(type(s), s)
    b, c = 2, 3
    print(b, c)
    c, b = b, c     # swaps the values
    print(b, c)
    tuple = (1, 2, 3, 4, 5)
    print(tuple)

if __name__ == "__main__": main()
