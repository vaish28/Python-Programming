# -*- coding: utf-8 -*-
"""


"""


# FIzzBuzz game


def FizzBuzz(r):
    for i in range(1,r):
        if (i%3 == 0) & (i%5 == 0):
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
             print(i)

FizzBuzz(61)
