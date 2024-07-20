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
            display_projects(projects)
        elif choice == 'f':
            print('Filter projects functionality goes here.')
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
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

def display_projects(projects):
    """Displays all incomplete and completed projects"""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects):
        print(project)

    print("Completed projects:")
    for project in sorted(completed_projects):
        print(project)


def add_new_project(projects):
    """can add a new item"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update project priorities and completion"""
    for index, project in enumerate(projects):
        print(f"{index} - {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]

    new_percentage = input("New percentage: ")
    new_priority = input("New priority: ")

    project.completion_percentage = int(new_percentage)
    project.priority = int(new_priority)

if __name__ == '__main__':
    main()