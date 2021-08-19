
# Sources to help to solutionate the problem
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
# https://stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list

if __name__ == '__main__':

    # The numbers to enter in the array
    n = int(input().strip())

    # The array
    a = list(map(int, input().rstrip().split()))

    print('Initial arrray: ', a)
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
    endPosition = len(a) - 1

    while endPosition > 0:
        swapPosition = 0
        counter = 0
        for item in range(endPosition):
            i = a[counter]
            currentValue = i
            nextValue = a[counter + 1]
            if currentValue > nextValue:
                tmp = i
                a[counter] = nextValue
                a[counter + 1] = currentValue
                swapPosition = counter
                numberOfSwaps += 1
            counter += 1
        endPosition = swapPosition

    print('Array is sorted in', numberOfSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[len(a) - 1])
