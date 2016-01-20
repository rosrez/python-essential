#!/bin/python3

def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)

                             #  VVVVV - THESE ARE OPTIONAL ARGS
def testfunc(this, that, other, *args):
    print(this, that, other, args)  # args is a tuple

if __name__ == "__main__": main()
