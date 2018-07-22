import csv
import random

class Data():

    #Public members
    
    def __init__(self, csv_fd = None):
        if(csv_fd != None):
            self.import_year(csv_fd)

    def __del__(self):
        pass

    def import_year(self, csv_fd):
        self.data = {}
        with open(csv_fd) as csvfile:
            file_object = csv.reader(csvfile, delimiter=' ', quotechar='|')
            #The CSV is a file in memory, save it to a 2-d list
            count = 0
            current_row = None
            for row in file_object:
                if count % 32 == 0:
                    current_row = self.data[str(row[0])] = []
                else:
                    current_row.append(row[0].split(','))
                count += 1

    def print_raw_data(self):
        print(self.data)

    def get_keys(self):
        return self.data.keys()

    def normalize(self, results):
        top = max(results.values())
        bottom = min(results.values())
        delta = top - bottom

        for team in results:
            results[team] = (results[team] - bottom)/delta

        return results

    def get_data(self, row, column, norm=True):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][row][column])
        if norm:
            self.normalize(results)
        return results

    def get_random_data(self, norm=True):
        results = {}
        for team in self.data:
            results[team] = random.random()
        if norm:
            self.normalize(results)
        return results