#!/bin/python3

def main():
    fh = open("lines.txt")
    # enumerate produces two elements: the index and the value
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    s = 'this is a string'
    for i, c in enumerate(s):
        print(i, c)

if __name__ == "__main__": main()

