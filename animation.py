from matplotlib import pyplot as plt, animation
import networkx as nx
import numpy as np
from agent import Agent
from graph import Graph

plt.rcParams["figure.figsize"] = [16, 9]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

lift = nx.DiGraph()
lift.add_edge(1, 2, weight=1)    #L
lift.add_edge(1, 4, weight=1)    #L
lift.add_edge(3, 4, weight=1)    #L
lift.add_edge(5, 4, weight=1)    #L

slope = nx.DiGraph()
slope.add_edge(2, 1,color='k', weight=1)    #B
slope.add_edge(2, 3,color='g', weight=1)    #B
slope.add_edge(4, 1,color='b', weight=1)    #B
slope.add_edge(4, 5,color='r', weight=1)    #B
slope.add_edge(5, 3,color='r', weight=1)    #B


# explicitly set positions
pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0), 4: (4, 0.255), 5: (5, 0.1)}
options = {
    "font_size": 12,
    "node_size": 2000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
colors = nx.get_edge_attributes(slope,'color').values()                                                                                                          

graph = Graph()
agents = []
for agent in range(1000):
    agents.append(Agent(graph, 1))

def animate(frame):

    nodes = np.zeros(5)
    edges = np.zeros(65)
    for agent in agents:
        agent.update()
        if agent._edge is not None:
            edges[int(agent._edge - 1)] += 1
        else:
            nodes[int(agent._node) -1] += 1

    positions = graph.component_population
    fig.clear()
    nx.draw_networkx(lift, pos,style="dashed", with_labels=False, **options)
    nx.draw_networkx(slope, pos, edge_color=colors, with_labels=False, connectionstyle="arc3,rad=0.1", **options)
    nx.draw_networkx_labels(
        lift, pos,
        labels={
            1: int(positions[1]),
            2: int(positions[2]),
            3: int(positions[3]),
            4: int(positions[4]),
            5: int(positions[5])
            },
            font_color='black',
            font_size='15'

    )
    nx.draw_networkx_edge_labels(
        lift, pos,
        edge_labels={
            (1, 2): int(positions[13]),
            (1, 4): int(positions[24]),
            (3, 4): int(positions[37]),
            (5, 4): int(positions[54])
        },
        font_color='black',
        label_pos=0.75,
        font_size='15'
    )
    nx.draw_networkx_edge_labels(
        slope, pos,
        edge_labels={
            (2, 1): int(positions[12]),
            (2, 3): int(positions[23]),
            (4, 1): int(positions[21]),
            (4, 5): int(positions[55]),
            (5, 3): int(positions[44]),
            },
        font_color='black', 
        font_size='15',
        label_pos=0.75,
        clip_on=False
    )

ani = animation.FuncAnimation(fig, animate, frames=1, interval=1000, repeat=True)

plt.show()