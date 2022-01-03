"""
Ref: https://www.hackerrank.com/challenges/30-nested-logic/problem?isFullScreen=false

Your local library needs your help! Given the expected and actual 
return dates for a library book, create a program that calculates 
the fine (if any).

INPUT SAMPLE:

9 6 2015 (Data returned)
6 6 2015 (Data due)

Two lines separated by a space containing 3 integers.

"""

# Fines

not_fine = 0

fine_per_day = 15

fine_per_month = 500

fine_per_year = 10000

# Time

max_days = 31
max_months = 12
max_years = 3000


def convert_int(val) -> int:
    return int(val)


class HackerDate:
    def __init__(self, list):
        self.day = list[0]
        self.month = list[1]
        self.year = list[2]

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


date_returned = None
date_due = None

for _ in range(2):
    d = input().split(' ')

    data = list(map(convert_int, d))

    if not date_returned:
        date_returned = HackerDate(data)
    else:
        date_due = HackerDate(data)


def get_hackos_by_day(days: int) -> int:
    return fine_per_day * days


def get_hackos_by_month(months: int) -> int:
    return fine_per_month * months


def get_hackos() -> int:
    assert (date_returned and date_due)

    same_year = date_returned.year <= date_due.year
    same_month = date_returned.month <= date_due.month
    same_day = date_returned.day <= date_due.day

    if date_returned.year < date_due.year:
        return not_fine

    # On time
    if same_day and same_month and same_year:
        return not_fine

    # Not days but same month
    if not same_day and same_month and same_year:
        return get_hackos_by_day(date_returned.day - date_due.day)

    if not same_month and same_year:
        return get_hackos_by_month(date_returned.month - date_due.month)

    if not same_year:
        return fine_per_year

    # Case not considered
    return -1


# Print the result
print(get_hackos())

# Another solution with tuple (from HackerRank)

rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
