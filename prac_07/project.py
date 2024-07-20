"""
CP1404/CP5632 Practical - project with class
expected time: 20 minutes
Actual time:
"""

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, "
                f"start: {self.start_date}, "
                f"priority: {self.priority} "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completetion: {self.completion_percentage}% ")