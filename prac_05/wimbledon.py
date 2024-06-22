"""
wimbledon
Estimate: 40 minutes
Actual:   minutes
"""
import csv
FILE_PATH = 'wimbledon.csv'


data = []
with open(FILE_PATH, "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    header = next(reader)
    for row in reader:
        data.append(row)
print(data)