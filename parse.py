import data
import scipy.io as sio
import numpy as np
import csv

def append_data(data, results):
    for key in results:
        results[key].append(data[key])

f = open("descripition.txt", 'w')
f.write("name\n")


_2010 = data.Data("./dataset/2010.csv")

results = {}
keys = _2010.get_keys()
for key in keys:
    results[key] = []

y = _2010.get_fg2_pct()
append_data(y, results)
f.write("2 Pt Field Goal Percent\r\n")

y = _2010.get_fg3_pct()
append_data(y, results)
f.write("3 Pt Field Goal Percent\n")

y = _2010.get_fg_pct()
append_data(y, results)
f.write("Total Field Goal Percent\n")

y = _2010.get_orb_pct()
append_data(y, results)
f.write("Offensive Rebounds Percent\n")

y = _2010.get_stl_pct()
append_data(y, results)
f.write("Steal Percent\n")

y = _2010.get_blk_pct()
append_data(y, results)
f.write("Block Percent\n")

with open("data.csv", "wb") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(results.keys())
   writer.writerows(zip(*results.values()))

f.close()
"""
fg2 = _2010.get_fg2_pct()



x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

print len(y)

sio.savemat('test.mat', dict(x=np.array(x1.values())))
"""
