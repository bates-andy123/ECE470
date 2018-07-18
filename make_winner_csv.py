import result
import csv

data = {}

RESULT = result.RESULT
for year in RESULT:
    data[year] = []
    for r in range(len(RESULT[year])):
        data[year].append(RESULT[year][r])

print(data)

for year in data:
    with open("./our_data/winners/" + str(year) + "_bracket.csv", "w") as outfile:
        #data["Team"] = row_names

        writer = csv.writer(outfile, delimiter=',', lineterminator='\n')

        writer.writerows(data[year])
