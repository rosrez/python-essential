#!/bin/python3

import sys

def main():
    print("import sys")
    print("Python version {}.{}.{}".format(*sys.version_info))
    print(sys.platform)

    # we can import modules (perhaps, conditionally) inside of a function
    import os
    print("import os")
    print("os.name:", os.name)
    print("path:", os.getenv('PATH'))
    print("Wordking dir:", os.getcwd())
    print("Random bytes from urandom", os.urandom(25))

    import urllib.request
    # page = urllib.request.urlopen('http://www.google.com')
    # for line in page: print(str(line, encoding = "utf_8"), end = "")
    
    import random
    print("import random")
    print(random.randint(1,1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print("Current time", now, ":", now.year, now.month, now.day, now.hour, now.minute, now.second)

if __name__ == "__main__": main()
