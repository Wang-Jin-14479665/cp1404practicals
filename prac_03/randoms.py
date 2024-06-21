import random

"""
What did you see on line 1?
6, 18, 8, 12

What was the smallest number you could have seen, what was the largest?
smallest is 5 largest is 20

What did you see on line 2?
7, 9, 9, 7, 5

What was the smallest number you could have seen, what was the largest?
smallest is 3 largest is 9

Could line 2 have produced a 4?
Impossible, only odd numbers between 3 and 10 (including 3) will appear in line2.

What did you see on line 3?
3.207482933371267, 3.9413634405993325, 5.078208315673125, 4.579650242987126, 2.6884619272081287

What was the smallest number you could have seen, what was the largest?
smallest is 2.5 largest is 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
number = random.randint(1, 100)
print(number)