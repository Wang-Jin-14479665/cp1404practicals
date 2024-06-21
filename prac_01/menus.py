MENU = "Welcome! Here is menus: \n (H)ello \n (G)oodbye \n (Q)uit"

name = input("Enter name: ")

print(MENU)
choice = input("Enter your choice >>> ").lower()

while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Good bye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Enter your choice >>> ").lower()
print("Finished. ")
