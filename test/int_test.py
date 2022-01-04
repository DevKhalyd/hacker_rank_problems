# A number in base 2 (Binary)
number = int("1011", 2)

# ** Calculate powers...
square = number ** 2

power = number ** 3

print(f"Square of {number} is {square} - Power: {power}")

print("========= BASIC TEST FINISHED =========")

# A X given number in base 10 (Decimal)
num = 10000

# Reduce its value to the half
powerOfNum = int(num ** (1/2)) + 1

print(f"{powerOfNum}")