#!/bin/python3

def main():
    d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}   # this is a dictionary: dictionaries are modifiable
    print(type(d),d)
    print("Unsorted items - straightforward iteration")
    for k in d:
        print(k, d[k])
    print("Sorted items (alphabetically, by key)")
    for k in sorted(d.keys()):
        print(k, d[k])

    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = "five"
    )
    print("Another definition of the dictionary")
    for k in d:
        print(k, d[k])
    print("Adding a value")
    d["seven"] = 7
    print(d)

if __name__ == "__main__": main()
