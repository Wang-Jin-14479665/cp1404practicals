"""
CP1404/CP5632 Practical - Guitar practical
expected time: 20 minutes
Actual time:
"""

import csv
from guitar import Guitar

FILE_NAME = 'guitars.csv'

def main():
    guitars = load_guitars()

    display_guitars(guitars)

    print('\nGuitars sorted by year:')
    guitars.sort()
    display_guitars(guitars)

    print('\nAdd new guitar here')
    name = input("Enter guitar name (or 'q' to quit): ")
    while name != 'q':
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Enter guitar name (or 'q' to quit): ")
    print('Program quit')

    save_guitars(guitars)

def load_guitars():
    """Load guitar in csv file"""
    guitars = []
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Print out the contents of the list"""
    for guitar in guitars:
        print(guitar)

def save_guitars(guitars):
    """Write the added guitar to a csv file"""
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

main()