from matplotlib import pyplot as plt, animation
import networkx as nx
import numpy as np

from agent import Agent
from graph import Graph

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

lift = nx.DiGraph()
lift.add_edge(1, 2, weight=1)   #L
lift.add_edge(1, 4, weight=1)    #L
lift.add_edge(3, 4, weight=1)    #L
lift.add_edge(5, 4, weight=1)    #L

slope = nx.DiGraph()
slope.add_edge(2, 1,color='k', weight=1)    #B
slope.add_edge(2, 3,color='g', weight=1)    #B
slope.add_edge(4, 1,color='b', weight=1)    #B
slope.add_edge(4, 5,color='r', weight=1)    #B
slope.add_edge(5, 3,color='r', weight=1)   #B


# explicitly set positions
pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0), 4: (4, 0.255), 5: (5, 0.1)}
options = {
    "font_size": 12,
    "node_size": 300,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
colors = nx.get_edge_attributes(slope,'color').values()                                                                                                          

graph = Graph()
agent = Agent(graph, 1)
agents = []
for agent in range(100000):
    agents.append(Agent(graph, 1))
Agent(graph, 1)
def animate(frame):

    nodes = np.zeros(5)
    edges = np.zeros(65)
    for agent in agents:
        agent.update()
        if agent._edge is not None:
            edges[int(agent._edge - 1)] += 1
        else:
            nodes[int(agent._node) -1] += 1

    fig.clear()                                                                                                         
    nx.draw_networkx(lift, pos,style="dashed", with_labels=False, **options)
    nx.draw_networkx(slope, pos, edge_color=colors, with_labels=False, connectionstyle="arc3,rad=0.1", **options)
    nx.draw_networkx_labels(
        lift, pos,
        labels={
            1: int(nodes[0]),
            2: int(nodes[1]),
            3: int(nodes[2]),
            4: int(nodes[3]),
            5: int(nodes[4])
            },
            font_color='black'
    )
    nx.draw_networkx_edge_labels(
        lift, pos,
        edge_labels={
            (1, 2): int(edges[12]),
            (1, 4): int(edges[23]),
            (3, 4): int(edges[36]),
            (5, 4): int(edges[53])
        },
        font_color='black',
        label_pos=0.75,
        font_size='15'
    )
    nx.draw_networkx_edge_labels(
        slope, pos,
        edge_labels={
            (2, 1): int(edges[11]),
            (2, 3): int(edges[22]),
            (4, 1): int(edges[20]),
            (4, 5): int(edges[54]),
            (5, 3): int(edges[43]),
            },
        font_color='black', 
        font_size='15',
        label_pos=0.75,
        verticalalignment='bottom',
        clip_on=False
    )

ani = animation.FuncAnimation(fig, animate, frames=6, interval=1000, repeat=True)

plt.show()
'''
G = nx.DiGraph()
G.add_edge(1, 2, weight=1)   #L
G.add_edge(1, 4, weight=1)    #L
G.add_edge(3, 4, weight=1)    #L
G.add_edge(5, 4, weight=1)    #L

slope = nx.DiGraph()
G.add_edge(2, 1,color='k', weight=1)    #B
G.add_edge(2, 3,color='g', weight=1)    #B
G.add_edge(4, 1,color='b', weight=1)    #B
G.add_edge(4, 5,color='r', weight=1)    #B
G.add_edge(5, 3,color='r', weight=1)   #B
pos = nx.spring_layout(G)

def animate(i):
    colors = ['r', 'b', 'g', 'y', 'w', 'm']
    nx.draw_circular(G, node_color=[np.random.choice(colors) for j in range(9)])

nx.draw_circular(G)
fig = plt.gcf()

# Animator call
anim = animation.FuncAnimation(fig, animate, frames=20, interval=20, blit=True)
'''