import result
import csv

data = {}

RESULT = result.RESULT
for year in RESULT:
    data[year] = [result.BRACKET_ORIG[year]]
    for r in range(len(RESULT[year])):
        data[year].append(RESULT[year][r])

lookup = {}		

for year in data:
	with open('our_data/lookup/' + str(year) + '_lookup.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		lookup[year] = {}
		for row in spamreader:
			lookup[year][row[0]] = row[1]
			
number = {}

for year in data:
	key = year -2000
	number[key] = []
	r = 0
	for	row in data[year]:
		number[key].append([])
		for col in row:
			number[key][r].append(lookup[year][col])
		r += 1
			
print(number[10])
print(data[2010])
#data.update(number)
#print(data[10])

for year in data:
	key = year - 2000
	for result in number[key]:
		data[year].append(result)
			
for year in data:
    with open("./our_data/winners/" + str(year) + "_bracket.csv", "w") as outfile:

        writer = csv.writer(outfile, delimiter=',', lineterminator='\n')

        writer.writerows(data[year])
