#!/bin/python3

def main():
    infile = open('lines.txt', 'r')
    outfile = open('out.tmp', 'w')
    for line in infile:
        # Note the named file parameter here, this is our output file.
        print(line, file = outfile, end='')
    print("Done.")

if __name__ == "__main__": main()
