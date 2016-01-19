#!/bin/python3

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # sub() is a search and replace function
        # sub(pattern, replacement, where)
        print(re.sub('(Len|Neverm)ore', '###', line), end='')

if __name__ == "__main__": main()
