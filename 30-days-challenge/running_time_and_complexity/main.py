"""
Task:

A prime is a natural number greater than 1 that has no positive 
divisors other than 1 and itself. Given a number,n , determine 
and print whether it is Prime or Not prime.

Ref:https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem?isFullScreen=true

"""

#  Enter your code here. Read input from STDIN. Print output to STDOUT

# NOTE: This code works for the first 10 numbers but what if I have a number bigger???

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

# https://www.hackerrank.com/challenges/30-running-time-and-complexity/forum/comments/722684

for _ in range(int(input())):
    num = int(input())
    if(num == 1):
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            # Range contains 3 parameters start, stop and step
            # start : Its because we are working just with odd numbers
            # step : We are working with odd numbers so we are skipping even numbers
            # stop : Get the square root of the number to dicrease that value if its a large number.
            # Add 1 to convert the value to upper bound
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")