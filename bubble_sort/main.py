import math
import os
import random
import re
import sys

if __name__ == '__main__':

    # The numbers to enter in the array
    n = int(input().strip())

    # The array
    a = list(map(int, input().rstrip().split()))

    # Goals output

    """
    1. Show the number of swaps
    2. Show the first element
    3. Show the last element

    Example:

    Input
    3
    3 2 1

    Output
    Array is sorted in 0 swaps.
    First Element: 1
    Last Element: 3
    """

    numberOfSwaps = 0

    for index, item in enumerate(a, start=1):
        # It´s not in it's own place
        if index != item:
            # Looking for that value
            for index2, i in enumerate(a):
                numberOfSwaps += 1
                if i == index:
                    a[index - 1] = i
                    a[index2] = item

    print('Array is sorted in ',numberOfSwaps,' swaps.')
    print('First Element: ', a[0])
    print('Last Element: ', a[len(a) - 1])


# Sources to help to solutionate the problem
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
# https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
