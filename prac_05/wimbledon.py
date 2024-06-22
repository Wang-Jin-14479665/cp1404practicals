"""
wimbledon
Estimate: 40 minutes
Actual:   50 minutes
"""
import csv
FILE_PATH = 'wimbledon.csv'

def main():
    data = process_data()
    champions = process_champions(data)
    countries = process_countries(data)
    display_champions(champions)
    display_countries(countries)

def process_data():
    """Use the imported csv processing file"""
    data = []
    with open(FILE_PATH, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)
        for row in reader:
            data.append(row)
    return data

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
    """Extract all the countries that won the championship"""
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)

def display_champions(champions):
    """Output processed championship results on request"""
    print("Wimbledon Champions: ")
    for champion, count in champions.items():
        print(f"{champion} {count}")

def display_countries(countries):
    """Export all winning countries according to the requirements and statistics"""
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(" ".join(countries))

main()