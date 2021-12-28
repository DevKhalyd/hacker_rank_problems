"""
Task:

A prime is a natural number greater than 1 that has no positive 
divisors other than 1 and itself. Given a number,n , determine 
and print whether it is Prime or Not prime.

Ref:https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

"""

#  Enter your code here. Read input from STDIN. Print output to STDOUT

# NOTE: This code works for the first 10 numbers but what if I have a number bigger???

# TODO: Complete with another algorithm

prime = 'Prime'
not_prime = 'Not prime'

T = int(input())

list = []

for i in range(T):
    n = int(input())
    val = None
    if n % n == 0 and n % 1 == 0:
        for index in range(2,7):
            if index == n:
                continue

            if n % index == 0:
                val = not_prime
            
            if val:
                break

        if not val:
            val = prime

    list.append(val)


for s in list:
    print(s)
