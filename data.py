import csv

class Data():

    #Public members
    data = {}
    
    def __init__(self, csv_fd = None):
        if(csv_fd != None):
            self.import_year(csv_fd)

    def import_year(self, csv_fd):
        with open(csv_fd, 'rb') as csvfile:
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
        print self.data

    def get_keys(self):
        return self.data.keys()

    def normalize(self, results):
        top = max(results.values())
        bottom = min(results.values())
        delta = top - bottom

        for team in results:
            results[team] = (results[team] - bottom)/delta

        return results

    def get_fg2_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][4][1])
        
        self.normalize(results)
        
        return results


    def get_fg2_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][3][1])
        
        self.normalize(results)
        
        return results

    def get_fg3_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][5][1])
        
        self.normalize(results)
        
        return results

    def get_fg_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][1][1])
        
        self.normalize(results)
        
        return results


    def get_orb_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][10][1])
        
        self.normalize(results)
        
        return results

    def get_stl_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][13][1])
        
        self.normalize(results)
        
        return results

    def get_blk_pct(self):
        results = {}
        for team in self.data:
            results[team] = float(self.data[team][14][1])
        
        self.normalize(results)
        
        return results