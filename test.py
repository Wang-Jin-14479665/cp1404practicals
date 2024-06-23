import csv


def load_data(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        header = next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data


def process_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def process_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


def display_champions(champions):
    print("Wimbledon Champions:")
    for champion, wins in champions.items():
        print(f"{champion} {wins}")


def display_countries(countries):
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    file_path = 'prac_05/wimbledon.csv'
    data = load_data(file_path)

    champions = process_champions(data)
    countries = process_countries(data)

    display_champions(champions)
    display_countries(countries)


main()
