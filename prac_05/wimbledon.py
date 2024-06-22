"""
wimbledon
Estimate: 40 minutes
Actual:   minutes
"""
import csv
FILE_PATH = 'wimbledon.csv'

def main():
    data = []
    with open(FILE_PATH, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        for row in reader:
            data.append(row)
    print(data)

    champions = process_champions(data)
    countries = processs_countries(data)

def process_champions(data):
    """Extract all champion names and number of championships from the data"""
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions

def process_countries(data):


main()