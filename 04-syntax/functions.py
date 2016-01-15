#!/bin/python3

def main():
    func()
    func_param(1)
    func_param()                    # the input parameter (a) assumes the default value (7) during this call
    func_param(5)

def func():
    for i in range(10):             # range(n) produces a range from 0 to n-1
        print(i, end = ' ')         # end = char, print statement ends with the specified character instead of default newline
    print()                         # this prints a newline at the end of the space-separated list

def func_param(a=7):
    for i in range(a, 10):
        print(i, end=' ')
    print()

if __name__ == "__main__": main()
