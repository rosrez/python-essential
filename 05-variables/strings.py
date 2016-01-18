#!/bin/python3

def main():
    s = 'This is a string!'
    print(s)

    s1 = "This is a \nstring!"
                #   ^^ - newline will be printed before 'string'
    print(s1)

    # If we want Python to treat the text literally, we precede the string constant with r.
    # This is called a raw string.
    # This is most often used when creating regular expressions.
    raw_string = r"This is a raw \nstring!"
    print(raw_string)

    # Python 3 way
    n = 42
    s = "This is a {} string!".format(n)
                #  ^^ format() method inserts its value here 
    print(s)

    # Pytnon 2 way
    n = 43
    s = "This is a %s string!" % n
    print(s)

    #      V - THE BACKSLASH ESCAPES THE NEWLINE CHARACTER SO IT DOESN'T APPEAR AT THE BEGINNING OF OUTPUT
    s = '''\
This is a string that can span several lines:
Line after line
after line
of text and more text.'''
    print(s)

if __name__ == "__main__": main()
