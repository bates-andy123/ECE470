import data
import scipy.io as sio
import numpy as np
import csv

results = {}
row_names = []

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

def generate_random_row(name, data):
    global results, row_names
    y = data.get_random_data()
    append_data(y, results, name)
    row_names.append(name)

years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016"]

for year in years:

    results = {}
    row_names = []
    keys = []
    #print(keys)

    year_obj = data.Data("./dataset/" + year + ".csv")
    keys = year_obj.get_keys()
    results["Team"] = []
    for key in keys:
        results[key] = []

    #print(len(results.keys()))

    add_new_field("2 Pt Field Goal Percent", year_obj, 3 ,1)
    add_new_field("3 Pt Field Goal Percent", year_obj, 5 ,1)
    add_new_field("Total Field Goal Percent", year_obj, 1 ,1)
    add_new_field("Offensive Rebounds Percent", year_obj, 10 ,1)
    add_new_field("Steal Percent", year_obj, 13 ,1)
    add_new_field("Block Percent", year_obj, 14 ,1)
    add_new_field("3 Pt Field Goal Attempts", year_obj, 6 ,1)
    add_new_field("2 Pt Field Goal Attempts", year_obj, 4 ,1)
    add_new_field("Total Field Goal Attempts", year_obj, 2 ,1)
    add_new_field("Opponent Points Per Game", year_obj, 27 ,1)
    add_new_field("Defense Rating", year_obj, 30, 1)
    add_new_field("Offense Rating", year_obj, 29 ,1)
    add_new_field("Opponent Assets", year_obj, 22 ,1)
    add_new_field("Opponent Offensive Rebounds", year_obj, 20 ,1)
    add_new_field("First Best Player Field Goal Percentage", year_obj, 1 ,3)
    add_new_field("Second Best Player Field Goal Percentage", year_obj, 1 ,4)
    add_new_field("Third Best Player Field Goal Percentage", year_obj, 1 ,5)
    add_new_field("Points Per Game", year_obj, 27 ,1)
    add_new_field("Opponent Field Personal Fouls", year_obj, 26 ,1)
    add_new_field("Opponent 3 Pt Field Goal Percentage", year_obj, 19 ,1)
    generate_random_row("Random 1", year_obj)
    generate_random_row("Random 2", year_obj)
    generate_random_row("Random 3", year_obj)
    generate_random_row("Random 4", year_obj)
    generate_random_row("Random 5", year_obj)

    with open("./our_data/training/" + year + "_data.csv", "w") as outfile:
       results["Team"] = row_names

       writer = csv.writer(outfile, delimiter=',', lineterminator='\n')
       writer.writerow(results.keys())
       writer.writerows(zip(*results.values()))

    f = open("./our_data/training/" + year + "_descripition.txt", 'w')
    for r in row_names:
        f.write(r + '\n')
    f.close()
