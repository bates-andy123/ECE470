import result
import csv

data = {}
RESULT = result.BRACKET_ORIG

for year in RESULT:
	count = 1
	data[year] = []
	for team in RESULT[year]:
		data[year].append([team, count])
		count += 1
		
for year in data:
    with open("./our_data/lookup/" + str(year) + "_lookup.csv", "w") as outfile:

        writer = csv.writer(outfile, delimiter=',', lineterminator='\n')

        writer.writerows(data[year])