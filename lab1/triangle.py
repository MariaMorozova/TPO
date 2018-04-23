#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

def isTriangle(a, b, c):
    return (a > 0 and b > 0 and c > 0 \
            and a + b > c \
            and b + c > a \
            and a + c > b)


def isNumber(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if (len (sys.argv) != 4):
        print ("The correct command line format:\ntriangle.exe <number> <number> <number>")
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[3]
        if (isNumber(a) & isNumber(b) & isNumber(c)):
            triangle = [float(a), float(b), float(c)]
            if isTriangle(triangle[0], triangle[1], triangle[2]):
                if triangle[0] == triangle[1] == triangle[2]:
                    print ("Triangle is equilateral")
                elif triangle[0] == triangle[1] or\
                triangle[1] == triangle[2] or\
                triangle[0] == triangle[2]:
                    print ("Triangle is isosceles")
                else:
                    print ("Triangle is normal")
            else:
                print ("It's not triagle")
        else:
            print ("One or more parameter isn't number")
