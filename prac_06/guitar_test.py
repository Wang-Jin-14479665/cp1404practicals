"""
guitar
Estimated time: 15 minutes
Actual time: 10 minutes
"""
from guitar import Guitar

guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 1512.9)

print(guitar1)
print(guitar2)

# Test get_age()
print(f"{guitar1.name} get_age() - Expected 102. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 11. Got {guitar2.get_age()}")

# Test is_vintage()
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
