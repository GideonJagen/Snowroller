import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

class Graph:
    def __init__(self, bansko) -> None:
        self.graph = self._init_graph(bansko)
        self.component_population = np.zeros(self.encode_slope(self.graph.number_of_nodes(), self.graph.number_of_nodes()) + 1)
        

    def _init_graph(self, bansko):
        graph = nx.DiGraph()
        if not bansko:
            graph.add_edge(1, 2, lift = True, queue = 0, capacity=53, time=3.5)
            graph.add_edge(1, 4, lift = True, queue = 0, capacity=23, time=5)
            graph.add_edge(3, 4, lift = True, queue = 0, capacity=20, time=3.5)
            graph.add_edge(5, 4, lift = True, queue = 0, capacity=17, time=1)

            #slope = nx.DiGraph()
            graph.add_edge(2, 1, lift = False, difficulty = 1, time = 3)
            graph.add_edge(2, 3, lift = False, difficulty = 0.25, time = 3)
            graph.add_edge(4, 1, lift = False, difficulty = 0.5, time = 3)
            graph.add_edge(4, 5, lift = False, difficulty = 0.75, time = 3)
            graph.add_edge(5, 3, lift = False, difficulty = 0.75, time = 3)
        else:
            graph.add_edge(1, 2, lift = True, queue = 0, time=10, capacity=33.3)    #bansko
            graph.add_edge(3, 2, lift = True, queue = 0, time=4, capacity=32.75)   #chalin valog
            graph.add_edge(2, 4, lift = True, queue = 0, time=11, capacity=33.3)   #bansko
            graph.add_edge(4, 5, lift = True, queue = 0, time=6.3, capacity=33.33)   #Banderitza 1
            graph.add_edge(4, 6, lift = True, queue = 0, time=2.5, capacity=50)   #Kolarski
            graph.add_edge(7, 6, lift = True, queue = 0, time=7.2, capacity=15.9)   #stara kotva
            graph.add_edge(8, 6, lift = True, queue = 0, time=6.5, capacity=15.9)   #detska kotva
            graph.add_edge(8, 9, lift = True, queue = 0, time=7, capacity=33.3)   #todorka
            graph.add_edge(5, 10, lift = True, queue = 0, time=3.5, capacity=33.33)  #Banderitza 2
            graph.add_edge(8, 11, lift = True, queue = 0, time=7.5, capacity=33.33)  #shiligarnik
            graph.add_edge(11, 10, lift = True, queue = 0, time=5.5, capacity=36.67) #Plato
            graph.add_edge(12, 11, lift = True, queue = 0, time=9.5, capacity=32.33) #mosta

            graph.add_edge(2, 3,difficulty=0.75, lift = False, time = 1)
            graph.add_edge(2, 3,difficulty=0.5, lift = False, time = 3)    # 2 Backar
            graph.add_edge(4, 1,difficulty=0.5, lift = False, time = 20)
            graph.add_edge(4, 3,difficulty=0.5, lift = False, time = 14)
            graph.add_edge(3, 1,difficulty=0.5, lift = False, time = 6)
            graph.add_edge(5, 4,difficulty=1, lift = False, time = 3)
            graph.add_edge(6, 7,difficulty=0.75, lift = False, time = 3)
            graph.add_edge(6, 8,difficulty=0.5, lift = False, time = 7)
            graph.add_edge(6, 8,difficulty=0.75, lift = False, time = 4)    #2 stycken
            graph.add_edge(8, 7,difficulty=0.5, lift = False, time = 6)
            graph.add_edge(7, 4,difficulty=0.5, lift = False, time = 8)
            graph.add_edge(8, 12,difficulty=0.5, lift = False, time = 6)
            graph.add_edge(9, 8,difficulty=0.75, lift = False, time = 6)
            graph.add_edge(9, 5,difficulty=0.75, lift = False, time = 4)
            graph.add_edge(5, 6,difficulty=0.75, lift = False, time = 3)
            graph.add_edge(10, 9,difficulty=0.75, lift = False, time = 3)
            graph.add_edge(10, 5,difficulty=0.75, lift = False, time = 10)
            graph.add_edge(10, 11,difficulty=0.5, lift = False, time = 14)
            graph.add_edge(9, 11,difficulty=0.5, lift = False, time = 8)
            graph.add_edge(11, 8,difficulty=0.5, lift = False, time = 8)
            graph.add_edge(11, 12,difficulty=0.5, lift = False, time = 7)
            graph.add_edge(12, 2,difficulty=0.25, lift = False, time = 4)
        return graph

    def _set_edge_attribute(self, edge, attribute, value):
        start, end = self.decode_slope(edge)
        self.graph[start][end][attribute] = value

    def get_neighbors(self, position):
        return self.graph[position]

    def encode_slope(self, start_node, end_node):
        # Cantor pairing function
        slope_index = ((start_node + end_node) * (start_node + end_node + 1))/2 + end_node + self.graph.number_of_nodes()
        return int(slope_index)

    def decode_slope(self, slope_index):
        # inverted Cantor pairing function
        d = slope_index - self.graph.number_of_nodes()
        w = np.floor((np.sqrt(8*d + 1) -1)/2)
        t = (np.square(w) + w)/2
        end_node = d - t
        start_node = w - end_node
        return int(start_node), int(end_node)

    def reposition_agent(self, current_position, new_position):
        self.component_population[current_position] -= 1
        self.component_population[new_position] += 1

    def get_edge_attribute(self, edge, attribute):
        start, end = self.decode_slope(edge)
        return self.graph[start][end][attribute]

    def enter_queue(self, edge):
        start, end = self.decode_slope(edge)
        self.graph[start][end]['queue'] += 1

    def leave_queue(self, edge):
        start, end = self.decode_slope(edge)
        self.graph[start][end]['queue'] -= 1

    def get_queues(self):
        queues = [
            self.graph[1][2]['queue'],
            self.graph[3][2]['queue'],
            self.graph[2][4]['queue'],
            self.graph[4][5]['queue'],
            self.graph[4][6]['queue'],
            self.graph[7][6]['queue'],
            self.graph[8][6]['queue'],
            self.graph[8][9]['queue'],
            self.graph[5][10]['queue'],
            self.graph[8][11]['queue'],
            self.graph[11][10]['queue'],
            self.graph[12][11]['queue'],
            ]
        return queues



def main():
    g = Graph(bansko=True)
    slope_index = g.encode_slope(12, 12)
    #start_node, end_node = g.decode_slope(4)
    print(slope_index)
    #print(start_node, end_node)

if __name__ == '__main__':
    main()
