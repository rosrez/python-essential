#!/bin/python3

def main():
    f = open('lines.txt', 'r')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()
