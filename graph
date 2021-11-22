import networkx as nx
import matplotlib.pyplot as plt

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
colors = nx.get_edge_attributes(slope,'color').values()                                                                                                          
options = {
    "font_size": 12,
    "node_size": 300,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 2,
}
nx.draw_networkx(lift, pos,style="dashed", **options)
nx.draw_networkx(slope, pos, edge_color=colors,connectionstyle="arc3,rad=0.1", **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
