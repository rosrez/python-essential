#!/bin/python3

import re

line = input("Enter line: ")
print("The line |" + line + "| will be searched for three consecutive digits")

pattern = re.compile(r'\d\d\d')
if re.search(pattern, line): print("found 3 digits")
else: print("didn't find 3 digits")
