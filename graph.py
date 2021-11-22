import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

class Graph():
    def __init__(self) -> None:
        self.graph = self._init_graph()
        self.component_population = np.zeros(self.encode_slope(self.graph.number_of_nodes(), self.graph.number_of_nodes()))
        

    def _init_graph(self):
        graph = nx.DiGraph()
        graph.add_nodes_from(range(0,8))
        graph.add_edge(0, 1, lift = True, queue = 10)
        graph.add_edge(1, 0, lift = True, queue = 10)
        return graph

    def get_neighbors(self, position):
        return self.graph[position]

    def encode_slope(self, start_node, end_node):
        # i(start, end) = ((start + end) * (start + end + 1))/2 + end + n_nodes
        slope_index = ((start_node + end_node) * (start_node + end_node + 1))/2 + end_node + self.graph.number_of_nodes()
        return int(slope_index)

    def count_component_population(self, agent_positions):
        self.component_population[:] = 0
        for agent_position in agent_positions:
            self.component_population[agent_position] += 1



def main():
    g = Graph()
    slope_index = g.encode_slope(7, 7)
    agent_positions = [1, 25, slope_index]
    g.count_component_population(agent_positions)
    print(g.component_population)
    nx.draw(g.graph)
    plt.show()


if __name__ == '__main__':
    main()