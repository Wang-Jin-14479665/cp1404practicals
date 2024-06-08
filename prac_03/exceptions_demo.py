"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur if the user inputs something that cannot be converted to an integer, such as a string or a floating-point number.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur if the user inputs 0 as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Can change the code to avoid a ZeroDivisionError by checking if the denominator is zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator again: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
