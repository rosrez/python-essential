#!/bin/python3

fh = open("lines.txt")
for line in fh.readlines():     # NOTE THE COLON!
    print(line, end='')         # THE BODY OF THE LOOP IS INDENTED!
