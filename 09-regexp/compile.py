#!/bin/python3

# Precompiled regular expressions work faster. 
# There is a number of extra options to re.compile() that allow you to modify behaviour of a regular expression.

import re

def main():
    fh = open('raven.txt')
    # Note: re.IGNORECASE also has a shorthand notation of re.I
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            # we can also perform substitution using the precompiled pattern;
            # again, this works faster than the regular re.sub() or line.replace()
            print(pattern.sub('###', line), end='')

if __name__ == "__main__": main()
