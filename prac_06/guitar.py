"""
guitar
Estimated time: 30 minutes
Actual time: 20 minutes
"""
CURRENT_YEAR = 2024


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): {self.cost:,.2f}"

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= 50


