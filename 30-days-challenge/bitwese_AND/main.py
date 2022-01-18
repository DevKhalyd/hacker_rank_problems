#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

import math

"""
Refs:
https://docs.microsoft.com/en-us/cpp/cpp/bitwise-and-operator-amp?view=msvc-170
https://dartpad.dev/?id Check the result of 1&2 expression
"""

def bitwiseAnd(N, K):
    """N: limit of the set of numbers
       K: The limit to return in this function
    """

    list = range(1, N)
    # Max Possible value
    mP = 0

    for val in list:

        A = val

        iterations = 0
        # Avoid iterate a lot of times more
        if mP != 0 and mP == K-1:
            break

        for x in range(val, N):
            iterations += 1
            B = x + 1

            # Not in the set of numbers
            if B > N:
                break

            if mP != 0 and mP == K-1:
                break

            result = A & B

            if result < K and result > mP:
                mP = result

    return mP


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Test not passed with 5 2...
    count = 2

    lim = 2

    res = bitwiseAnd(count, lim)

    print(f"Result is: {res}")
