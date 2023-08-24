from zad2testy import runtests

class Node:
    def __init__(self):
        self.edges = []
        self.weights = []
        self.ids = []
        self.sum_of_edges = 0

    def addEdge(self, x, w, id):
        self.edges.append(x)
        self.weights.append(w)
        self.ids.append(id)


def balance( T ):
    """tu prosze wpisac wlasna implementacje"""
    return -1

    
runtests( balance )


