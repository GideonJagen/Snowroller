import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
import math

class Graph:
    def __init__(self) -> None:
        self.graph = self._init_graph()
        self.component_population = np.zeros(self.encode_slope(self.graph.number_of_nodes(), self.graph.number_of_nodes()) + 1)
        

    def _init_graph(self):
        graph = nx.DiGraph()
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
        queues = [self.graph[1][2]['queue'], self.graph[1][4]['queue'], self.graph[3][4]['queue'], self.graph[5][4]['queue']]
        return queues



def main():
    g = Graph()
    slope_index = g.encode_slope(0, 0)
    start_node, end_node = g.decode_slope(4)
    print(slope_index)
    print(start_node, end_node)

if __name__ == '__main__':
    main()
