"""

Task:

Consider a database table, Emails, which has the attributes
First Name and Email ID. Given N  rows of data simulating 
the Emails table, print an alphabetically-ordered list of 
people whose email address ends in @gmail.com.


Constraints

2 <= N <= 30

-Each of the first names consists of lower case letters  [a-z]  only.

-Each of the email IDs consists of lower case letters [a-z],@  and . only.

-The length of the first name is no longer than 20.

-The length of the email ID is no longer than 50.

"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]