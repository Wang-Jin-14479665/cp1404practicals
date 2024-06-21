numbers = []

for i in range(5):
    number = float(input(f"Enter {i + 1} numbers:"))
    numbers.append(number)
    # print(numbers)

first_number = int(numbers[0])
last_number = int(numbers[-1])
smallest = int(min(numbers))
largest = int(max(numbers))
average = sum(numbers) / len(numbers)

print(f"The first number is {first_number}\nThe last number is {last_number}\n"
      f"The smallest number is {smallest}\nThe largest number is {largest}\nThe average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")