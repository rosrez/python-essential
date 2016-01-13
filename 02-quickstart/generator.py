#!/bin/python3

def isprime(n):
    if (n == 1):
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# The yield statement returns the function's result, just as return does.
# The only exception is that the next time the function is called, 
# it will continue execution AFTER the previously invoked yield statement (n += 1, in this case).

# so primes() becomes an iterator/generator function that is suitable for a for-loop 
# to iterate through a list of values

def primes(n = 1):
    while (True):
        if isprime(n): yield n  # NOTE THE yield INSTEAD OF return
        n += 1

for n in primes():
    if n > 100: break
    print(n)
