#!/bin/python3

# compare to replace-sub.py which does almost the same thing using the re.sub() function.

import re

def main():
    fh = open('raven.txt')
    for line in fh:
        match = re.search('(Len|Neverm)ore', line)
        # we narrow down the output only to matching lines
        if match:
            print(line.replace(match.group(), "###"), end='')

if __name__ == "__main__": main()
