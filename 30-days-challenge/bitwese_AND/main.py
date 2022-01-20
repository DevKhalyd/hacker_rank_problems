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

# TODO: Test the 5 case

def bitwiseAnd(N, K):

    mp = 0

    A = K - 1

    for x in range(A, N):
        B = x + 1

        if B > N:
            break

        result = A & B

        if result < K and result > mp:
            mp = result

    return mp


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    count = 625

    lim = 457

    res = bitwiseAnd(count, lim)

    print(f"Result is: {res}")
