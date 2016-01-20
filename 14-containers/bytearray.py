#!/bin/python3

def main():
    # encoding = "utf_8" is meaningful to Python;
    # we must use it if the file's encoding is UTF-8
    fin = open('utf8.txt', 'r', encoding = 'utf_8')
    fout = open('utf8.html', 'w')
    
    # we use bytearray as an accumulator of converted characters
    outbytes = bytearray()
    for line in fin:
        # a string is an iterable object, so iterate through it
        for c in line:
            # ord(c) integer code of the character
            # if the character code is greater than 127 (non-ASCII),
            # generate an immutable byte array (bytes() constructor)
            # and pass it the following string as the argument
            # &#0000, where instead 0000 there is a character code
            if ord(c) > 127:
                # += operator on a mutable container type appends more than one element at a time
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = "utf_8")
            else: 
                outbytes.append(ord(c))
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print('Done.')

if __name__ == "__main__": main()
