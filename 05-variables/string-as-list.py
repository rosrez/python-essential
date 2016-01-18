#!/bin/python3

def main():
    x = 'string'
    print(type(x), x)
    print("character #2:", x[2])
    print("sliced 2:4", x[2:4])
    #                   ^^^^^^  -- prints characters [2;4)

if __name__ == "__main__": main()
