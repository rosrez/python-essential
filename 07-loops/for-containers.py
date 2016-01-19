#!/bin/python3

# all container types can serve as an iterator

def main():
    # tuple
    t = (1, 2, 3, 4, 5)
    print("tuple")
    for i in t:
        print(i, end=' ')
    print()

    # list
    l = [1, 2, 3, 4, 5]
    for i in l:
        print(i, end=' ')
    print()

    # dictionary
    d = dict(
        one = 1,
        two = 2,
        three = 3,
        four = 4,
        five = 5
    )
    for i in d:
        print(i)
    print()

    s = "string"
    for i in s:
        print(i, end=" ")
    print()

if __name__ == "__main__": main()
