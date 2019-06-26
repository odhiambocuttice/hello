import csv

records = []
with open('claims_data.csv') as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        if row[2] == '4321' and row[1] == 'F' and row[6]:
            # if row[2] == "4321":
            print(row[2], row[1], row[6])

total = 0
for i in range(len(row[6])):
    tt = row[i]
    total += float(tt)
    print(total)

records.append(row)


# record = enumerate(records, 1)
# print (records)
# print ('{}'.format())
# print(sum(int(row[6][7])))
