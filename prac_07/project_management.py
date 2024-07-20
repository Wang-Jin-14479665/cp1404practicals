"""
CP1404/CP5632 Practical - project_management
expected time: 60 minutes
Actual time:
"""
FILE_PATH = 'projects.txt'
MENU = ('- (L)oad projects'
        '\n- (S)ave projects'
        '\n- (D)isplay projects'
        '\n- (F)ilter projects by date'
        '\n- (A)dd new project'
        '\n- (U)pdate project'
        '\n- (Q)uit')
def main():
    print('Welcome to Pythonic Project Management')
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            print('Load projects functionality goes here.')
        elif choice == 's':
            print('Save projects functionality goes here.')
        elif choice == 'd':
            print('Display projects functionality goes here.')
        elif choice == 'f':
            print('Filter projects functionality goes here.')
        elif choice == 'a':
            print('Add new project functionality goes here.')
        elif choice == 'u':
            print('Update project functionality goes here.')
        else:
            print("Invalid choice")
        choice = input(">>> ").lower()

    save_choice = input("Would you like to save to projects.txt? (yes/no) ").lower()
    if save_choice == 'yes':
        print("Saving projects...")
    print("Thank you for using custom-built project management software.")

if __name__ == '__main__':
    main()