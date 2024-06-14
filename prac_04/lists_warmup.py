numbers = [3, 1, 4, 1, 5, 9, 2]

"""
numbers[0]            result: 3
numbers[-1]           result: 2
numbers[3]            result: 1
numbers[:-1]          result: [3, 1, 4, 1, 5, 9]
numbers[3:4]          result: [1,]
5 in numbers          result: True
7 in numbers          result: False
"3" in numbers        result: False
numbers + [6, 5, 3]   result: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers[0] = 'ten'  # Change the first element of numbers to "ten" (the string, not the number 10)
numbers[-1] = 1  # Change the last element of numbers to 1
print(numbers[2:])  # Print all the elements from numbers except the first two (slice)
print(9 in numbers)  # Print whether 9 is an element of numbers

