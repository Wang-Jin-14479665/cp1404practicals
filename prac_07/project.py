"""
CP1404/CP5632 Practical - project with class
expected time: 20 minutes
Actual time:
"""
from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, "
                f"start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority} "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}% ")

    def __repr__(self):
        # return (f"{self.name}, "
        #         f"start: {self.start_date}, "
        #         f"priority: {self.priority} "
        #         f"estimate: ${self.cost_estimate:.2f}, "
        #         f"completion: {self.completion_percentage}% ")
        return self.__str__()

    def is_complete(self):
        """Determine whether the project progress is complete"""
        return self.completion_percentage == 100


def run_tests():
    """Run simple tests/demos on Project class."""

    project1 = Project("Project 1", "01/03/2011", 1, 10000, 50)
    print(project1)

    project2 = Project("Project 2", "10/06/2022", 2, 2000.0, 75)
    print(project2)


if __name__ == "__main__":
    run_tests()
