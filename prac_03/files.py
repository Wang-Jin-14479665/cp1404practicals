name = input("Enter a nane: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# Task 2: Read the name from name.txt and print a greeting
file = open('name.txt', 'r')
name_from_file = file.read()
file.close()
print(f"Hi {name_from_file}!")

# Task 3: Read only the first two numbers from numbers.txt, add them, and print the result
with open('numbers.txt', 'r') as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())

result = first_number + second_number
print(result)