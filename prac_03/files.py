name = input("Enter a nane: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# Task 2: Read the name from name.txt and print a greeting
file = open('name.txt', 'r')
name_from_file = file.read()
file.close()

print(f"Hi {name_from_file}!")