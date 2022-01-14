#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

"""
Refs:


https://docs.microsoft.com/en-us/cpp/cpp/bitwise-and-operator-amp?view=msvc-170

https://dartpad.dev/?id Check the result of 1&2 expression

"""

# TODO: Test against the hacker rank test


def bitwiseAnd(N, K):
    """N: limit of the set of numbers
       K: The limit to return in this function
    """

    list = range(1, N)
    # Max Possible
    mP = 0

    for val in list:

        A = val

        # As a possible solution is to get the root of N...
        for x in range(val, N):
            B = x + 1

            if B > N:
                break

            result = A & B

            if result < K and result > mP:
                mP = result

    return mP


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Test not passed with 5 2...
    count = 8

    lim = 5

    res = bitwiseAnd(count, lim)

    print(f"Result is: {res}")
