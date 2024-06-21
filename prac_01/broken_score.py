"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

# Error 1: Line 17 print statement indent error
# Corrected code:

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
        print("Excellent")
if score < 50:
    print("Bad")

# At this point, the code is ready to run, but the partition of the decision structure is still unclear,
# and the code can also be updated as follows:

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")

