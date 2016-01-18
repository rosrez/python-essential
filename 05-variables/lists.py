#!/bin/python3

def main():
    x = [1, 2, 3]   # this is a list: lists are modifiable
    x.append(5)
    x.insert(0, 7)  # insert 7 at the beginning (before item 0)
    print(type(x),x)

if __name__ == "__main__": main()
