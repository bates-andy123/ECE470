from gene import Gene

GENES_PER_CHROMSOME = 5

class Chromsome():
    
    genes = [] 

    def __init__(self):
        self.genes.append(Gene())

    def add_gene(self):
        pass

    def remove_gene(self):
        pass