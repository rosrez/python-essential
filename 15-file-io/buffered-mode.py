#!/bin/python3

def main():
    buffersize = 10
    infile = open('lines.txt', 'r')
    outfile = open('out.tmp', 'w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)
    print("Done.")

if __name__ == "__main__": main()
