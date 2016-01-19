#!/bin/python3

def main():
    s = 'this is a string'
    print("The entire string", s)
    print("Now skipp all s letters", s)
    for c in s:
        # skip the letter 's'
        if c == 's': continue
        print(c, end='')
    print()

    print("Stop iterating at the first letter s")
    for c in s:
        # break out of the loop at the letter 's'
        if c == 's': break
        print(c, end='')
    print()

    print("Use else")
    for c in s:
        print(c, end='')
    else:                               # gets invoked when iteration stops (or never starts)
        print('<< iteration is over')

    print("Use else with a while loop")
    i = 0
    while (i < len(s)):
        print(s[i], end='')
        i += 1
    else:
        print('<< iteration is over')
   

if __name__ == "__main__": main()
