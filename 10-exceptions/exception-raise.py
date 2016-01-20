#!/bin/python3

import sys

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        # raise our own exception;
        # if uncaught, the Python interpreter will display a traceback
        raise ValueError('Filename must end with .txt')

def main():
    if len(sys.argv) < 2:
        print("Usage exceptions.py <filename>")
        exit(1)

    try:
        for line in readfile(sys.argv[1]): print(line.strip())
    except IOError as e:
        print('Could not open the file:', e)
    except ValueError as e:
        print('Bad filename:', e)

    # again, multiple except clauses may follow for different exception types

if __name__ == "__main__": main()
