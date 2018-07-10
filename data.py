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
                    current_row = self.data[str(row)] = []
                else:
                    current_row.append(row[0].split(','))
                count += 1
            
    def print_raw_data(self):
        print self.data