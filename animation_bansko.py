from matplotlib import pyplot as plt, animation
import networkx as nx
import numpy as np
from agent import Agent
from graph import Graph

plt.rcParams["figure.figsize"] = [16, 9]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

lift = nx.DiGraph()     #weight, tid, people/tid, allt i min
lift.add_edge(1, 2, weight=1, time=10, pph=33.3)    #bansko
lift.add_edge(3, 2, weight=1, time=4, pph=32.75)   #chalin valog
lift.add_edge(2, 4, weight=1, time=11, pph=33.3)   #bansko
lift.add_edge(4, 5, weight=1, time=6.3, pph=33.33)   #Banderitza 1
lift.add_edge(4, 6, weight=1, time=2.5, pph=50)   #Kolarski
lift.add_edge(7, 6, weight=1, time=7.2, pph=15.9)   #stara kotva
lift.add_edge(8, 6, weight=1, time=6.5, pph=15.9)   #detska kotva
lift.add_edge(8, 9, weight=1, time=7, pph=33.3)   #todorka
lift.add_edge(5, 10, weight=1, time=3.5, pph=33.33)  #Banderitza 2
lift.add_edge(8, 11, weight=1, time=7.5, pph=33.33)  #shiligarnik
lift.add_edge(11, 10, weight=1, time=5.5, pph=36.67) #Plato
lift.add_edge(12, 11, weight=1, time=9.5, pph=32.33) #mosta



slope = nx.DiGraph()
slope.add_edge(2, 3,color='r', weight=1)
slope.add_edge(2, 3,color='b', weight=1)    # 2 Backar
slope.add_edge(4, 1,color='b', weight=1)
slope.add_edge(4, 3,color='b', weight=1)
slope.add_edge(3, 1,color='b', weight=1)
slope.add_edge(5, 4,color='k', weight=1)
slope.add_edge(6, 7,color='r', weight=1)
slope.add_edge(6, 8,color='b', weight=1)
slope.add_edge(6, 8,color='r', weight=1)    #2 stycken
slope.add_edge(8, 7,color='b', weight=1)
slope.add_edge(7, 4,color='b', weight=1)
slope.add_edge(8, 12,color='b', weight=1)
slope.add_edge(9, 8,color='r', weight=1)
slope.add_edge(9, 5,color='r', weight=1)
slope.add_edge(5, 6,color='r', weight=1)
slope.add_edge(10, 9,color='r', weight=1)
slope.add_edge(10, 5,color='r', weight=1)
slope.add_edge(10, 11,color='b', weight=1)
slope.add_edge(9, 11,color='b', weight=1)
slope.add_edge(11, 8,color='b', weight=1)
slope.add_edge(11, 12,color='b', weight=1)
slope.add_edge(12, 2,color='g', weight=1)


# explicitly set positions
pos = {1: (0.9,0),2:(1.3,8),3:(1.3,4),4:(2.15,11),5:(1.87,22),6:(1.8,17),7:(1.75,12),8:(1.55,14),9:(1.85,30),10:(1.9,36),11:(1.4,27),12:(1.3,13)}
colors = nx.get_edge_attributes(slope,'color').values()                                                                                                          
options = {
    "font_size": 9,
    "node_size": 1000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1.2,
    "width": 1.4,
}                                                                                                     

graph = Graph(bansko=True)
agents = []
for agent in range(4000):
    agents.append(Agent(graph, 1))

def animate(frame):

    for agent in agents:
        agent.update()

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
            5: int(positions[5]),
            6: int(positions[6]),
            7: int(positions[7]),
            8: int(positions[8]),
            9: int(positions[9]),
            10: int(positions[10]),
            11: int(positions[11]),
            12: int(positions[12]),
            },
            font_color='black',
            font_size='11'

    )
    nx.draw_networkx_edge_labels(
        lift, pos,
        edge_labels={
            (1, 2): positions[graph.encode_slope(1, 2)],
            (3, 2): positions[graph.encode_slope(3, 2)],
            (2, 4): positions[graph.encode_slope(2, 4)],
            (4, 5): positions[graph.encode_slope(4, 5)],
            (4, 6): positions[graph.encode_slope(4, 6)],
            (7, 6): positions[graph.encode_slope(7, 6)],
            (8, 6): positions[graph.encode_slope(8, 6)],
            (5, 10): positions[graph.encode_slope(5, 10)],
            (8, 11): positions[graph.encode_slope(8, 11)],
            (8, 9): positions[graph.encode_slope(8, 9)],
            (11, 10): positions[graph.encode_slope(11, 10)],
            (12, 11): positions[graph.encode_slope(12, 11)],
        },
        font_color='black',
        label_pos=0.75,
        font_size='11'
    )
    nx.draw_networkx_edge_labels(
        slope, pos,
        edge_labels={
            (2, 3): int(positions[graph.encode_slope(2,3)]),
            (2, 3): int(positions[graph.encode_slope(2,3)]),
            (4, 1): int(positions[graph.encode_slope(4, 1)]),
            (4, 3): int(positions[graph.encode_slope(4, 3)]),
            (3, 1): int(positions[graph.encode_slope(3, 1)]),
            (5, 4): int(positions[graph.encode_slope(5, 4)]),
            (6, 7): int(positions[graph.encode_slope(6, 7)]),
            (6, 8): int(positions[graph.encode_slope(6, 8)]),
            (6, 8): int(positions[graph.encode_slope(6, 8)]),
            (8, 7): int(positions[graph.encode_slope(8, 7)]),
            (7, 4): int(positions[graph.encode_slope(7, 4)]),
            (8, 12): int(positions[graph.encode_slope(8, 12)]),
            (9, 8): int(positions[graph.encode_slope(9, 8)]),
            (9, 5): int(positions[graph.encode_slope(9, 5)]),
            (5, 6): int(positions[graph.encode_slope(5, 6)]),
            (10, 9): int(positions[graph.encode_slope(10, 9)]),
            (10, 5): int(positions[graph.encode_slope(10, 5)]),
            (10, 11): int(positions[graph.encode_slope(10, 11)]),
            (9, 11): int(positions[graph.encode_slope(9, 11)]),
            (11, 8): int(positions[graph.encode_slope(11, 8)]),
            (11, 12): int(positions[graph.encode_slope(11, 12)]),
            (12, 2): int(positions[graph.encode_slope(12, 2)]),
            },
        font_color='black', 
        font_size='11',
        label_pos=0.75,
        clip_on=False
    )

ani = animation.FuncAnimation(fig, animate, frames=1, interval=1000, repeat=True)

plt.show()