#!/bin/python3

fh = open("lines.txt")

# for-loops work with iterators, 
# i.e. they put consecutive values returned by an iterator in a control variable.
# fh.readlines() below is an iterator function

for line in fh.readlines():     # NOTE THE COLON!
    print(line, end='')         # THE BODY OF THE LOOP IS INDENTED!
