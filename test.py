
"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: Set is_finished to True to break the loop
    except ValueError:  # TODO: Catch ValueError exception for invalid integer input
        print("Please enter a valid integer.")
print("Valid result is:", result)
