import csv
records = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        gender = 'F'
        if gender in row[2]:
            records.append(row[0])

print(records)
