#!/bin/python3

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        # this captures our match
        match = re.search('(Len|Neverm)ore', line)
        # we can test the match for non-emptiness like this
        if match:
            # and here we print the matching part of the string 
            print(match.group())

if __name__ == "__main__": main()
