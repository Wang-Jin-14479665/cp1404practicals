name = input("Enter a nane: ")

file = open("name.txt", "w")

file.write(name)

file.close()