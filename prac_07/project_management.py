"""
CP1404/CP5632 Practical - project_management
expected time: 60 minutes
Actual time:
"""
from prac_07.project import Project

FILE_PATH = 'projects.txt'
MENU = ('- (L)oad projects'
        '\n- (S)ave projects'
        '\n- (D)isplay projects'
        '\n- (F)ilter projects by date'
        '\n- (A)dd new project'
        '\n- (U)pdate project'
        '\n- (Q)uit')
def main():
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILE_PATH}")

    print('Welcome to Pythonic Project Management')
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_projects()
            for row in projects:
                print(row)
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


def load_projects():
    """Read and load the data in the specified file"""
    projects = []
    with open(FILE_PATH, "r") as file:
        file.readline()  # Skip header
        for line in file:
            name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


if __name__ == '__main__':
    main()