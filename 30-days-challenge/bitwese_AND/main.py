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
# Rewrite this function with the new data found and test against the problems
def bitwiseAnd(n, k):

    pass


def bitwiseAnd2(N, K):
    """N: limit of the set of numbers
       K: The limit to return in this function
    """

    list = range(1, N)
    # Max Possible value
    mP = 0

    for val in list:

        # TODO: Just use K - 1
        A = K - 1

        iterations = 0
        # Avoid iterate a lot of times more
        if mP != 0 and mP == K-1:
            break

        for x in range(A, N):
            iterations += 1
            B = x + 1

            # Not in the set of numbers
            if B > N:
                break

            result = A & B

            print(f"{A} & {B} = {result}. Find Min: {K - 1}")

            if result < K and result > mP:
                mP = result

            if mP != 0 and mP == K-1:
                break

    return mP


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Test not passed with 5 2...

    # TODO:Test the other cases

    count = 614

    lim = 327
    # Expected 103 getting 106. Why?

    res = bitwiseAnd(count, lim)

    print(f"Result is: {res}")
