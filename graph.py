import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

class Graph():
    def __init__(self) -> None:
        self.graph = self._init_graph()
        self.component_population = np.zeros(self.encode_slope(self.graph.number_of_nodes(), self.graph.number_of_nodes()) + 1)
        

    def _init_graph(self):
        graph = nx.DiGraph()
        graph.add_edge(1, 2, lift = True, queue = 0 capacity=3200, time=3.5)    #L
        graph.add_edge(1, 4, lift = True, queue = 0, capacity=1400, time=5)    #L
        graph.add_edge(3, 4, lift = True, queue = 0, capacity=1200, time=3.5)    #L
        graph.add_edge(5, 4, lift = True, queue = 0, capacity=1000, time=1)    #L

        #slope = nx.DiGraph()
        graph.add_edge(2, 1, lift = False, difficulty = 1,)    #B
        graph.add_edge(2, 3, lift = False, difficulty = 0.25)    #B
        graph.add_edge(4, 1, lift = False, difficulty = 0.5)    #B
        graph.add_edge(4, 5, lift = False, difficulty = 0.75)    #B
        graph.add_edge(5, 3, lift = False, difficulty = 0.75)    #B
        return graph

    def get_neighbors(self, position):
        return self.graph[position]

    def encode_slope(self, start_node, end_node):
        # Cantor pairing function
        slope_index = ((start_node + end_node) * (start_node + end_node + 1))/2 + end_node + self.graph.number_of_nodes()
        return int(slope_index)

    def decode_slope(self, slope_index):
        # inverted Cantor pairing function
        slope_index = slope_index - self.graph.number_of_nodes()
        w = np.floor((np.sqrt(8*slope_index + 1) -1)/2)
        t = (np.square(w) + w)/2
        end_node = slope_index - t
        start_node = w - end_node
        return start_node, end_node

    def count_component_population(self, agent_positions):
        self.component_population[:] = 0
        for agent_position in agent_positions:
            self.component_population[agent_position] += 1



def main():
    g = Graph()
    slope_index = g.encode_slope(2, 2)
    start_node, end_node = g.decode_slope(slope_index)
    print(start_node)
    print(end_node)

if __name__ == '__main__':
    main()
