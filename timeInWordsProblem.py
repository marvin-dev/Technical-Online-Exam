#!/bin/python3
# MARVIN BANTON

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    time = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine",
    ]

    if m == 0:
        print(time[h], "o' clock")
    elif m == 1:
        print("one minute past", time[h])
    elif m == 59:
        print("one minute to", time[(h % 12) + 1])
    elif m == 15:
        print("quarter past", time[h])
    elif m == 30:
        print("half past", time[h])
    elif m == 45:
        print("quarter to", time[(h % 12) + 1])
    elif m <= 30:
        print(time[m], "minutes past", time[h])
    elif m > 30:
        print(time[60 - m], "minutes to", time[(h % 12 + 1)])

h = int(input("Hours: "))
m = int(input("Minutes: "))

timeInWords(h, m)