import data
import scipy.io as sio
import numpy as np
import csv

results = {}
row_names = []

_2010 = data.Data("./dataset/2010.csv")
keys = _2010.get_keys()
results["Team"] = []
for key in keys:
    results[key] = []


def append_data(data, results, name):
    for key in results:
        if key == "Team":
            results[key].append(name)
        else:
            results[key].append(data[key])

def add_new_field(name, data, row, column):
    global results, row_names
    y = data.get_data(row, column)
    append_data(y, results, name)
    row_names.append(name)

add_new_field("2 Pt Field Goal Percent", _2010, 3 ,1)
add_new_field("3 Pt Field Goal Percent", _2010, 5 ,1)
add_new_field("Total Field Goal Percent", _2010, 1 ,1)
add_new_field("Offensive Rebounds Percent", _2010, 10 ,1)
add_new_field("Steal Percent", _2010, 13 ,1)
add_new_field("Block Percent", _2010, 14 ,1)


with open("data.csv", "w") as outfile:
   results["Team"] = row_names

   writer = csv.writer(outfile)
   writer.writerow(results.keys())
   writer.writerows(zip(*results.values()))

f = open("descripition.txt", 'w')
for r in row_names:
    f.write(r + '\n')
f.close()
