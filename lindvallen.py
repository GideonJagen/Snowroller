import networkx as nx
import matplotlib.pyplot as plt

lift = nx.DiGraph()
lift.add_edge(1, 2, weight=1)    #L
lift.add_edge(4, 5, weight=1)    #L
lift.add_edge(4, 6, weight=1)    #L
lift.add_edge(8, 9, weight=1)    #2 liftar
lift.add_edge(11, 12, weight=1)    #2 liftar
lift.add_edge(13, 14, weight=1)    #3 liftar
lift.add_edge(16, 17, weight=1)    #3 liftar
lift.add_edge(20, 21, weight=1)


slope = nx.DiGraph()
slope.add_edge(2, 1,color='k', weight=1)
slope.add_edge(2, 1,color='k', weight=1)    # 2 Backar
slope.add_edge(2, 3,color='r', weight=1)    
slope.add_edge(3, 1,color='r', weight=1)    
slope.add_edge(5, 6,color='b', weight=1)    
slope.add_edge(5, 3,color='r', weight=1)   
slope.add_edge(6, 4,color='b', weight=1)  
slope.add_edge(5, 7,color='r', weight=1)  
slope.add_edge(7, 6,color='r', weight=1) 
slope.add_edge(7, 3,color='r', weight=1)    
slope.add_edge(9, 6,color='b', weight=1)    
slope.add_edge(9, 10,color='r', weight=1)    
slope.add_edge(6, 8,color='b', weight=1)    
slope.add_edge(10, 8,color='r', weight=1)  
slope.add_edge(12, 10,color='r', weight=1)    
slope.add_edge(10, 11,color='r', weight=1)    
slope.add_edge(12, 11,color='b', weight=1)
slope.add_edge(12, 11,color='k', weight=1)  #2 backar
slope.add_edge(14, 15,color='b', weight=1)
slope.add_edge(15, 13,color='b', weight=1)
slope.add_edge(17, 15,color='b', weight=1)
slope.add_edge(15, 16,color='b', weight=1)

slope.add_edge(12, 18,color='r', weight=1)
slope.add_edge(18, 19,color='r', weight=1)
slope.add_edge(14, 18,color='b', weight=1)
slope.add_edge(18, 13,color='b', weight=1)
slope.add_edge(18, 13,color='r', weight=1) #2backar
slope.add_edge(14, 13,color='r', weight=1)
slope.add_edge(19, 13,color='r', weight=1)
slope.add_edge(19, 11,color='r', weight=1)


# explicitly set positions
pos = {1: (0, 0), 2: (0, 8), 3: (0.5, 4), 4:(1,0),5:(1,8)
       ,6:(1.5,3),7:(0.7,6),8:(2,0),9:(2,8),10:(2.5,3.5),11:(3,0),
       12:(3,8),13:(5,0),14:(5,8),15:(5.4,4),16:(6,0),17:(6,8),
       18:(4,6),19:(4,2),20:(8,0),21:(8,8)}
colors = nx.get_edge_attributes(slope,'color').values()                                                                                                          
options = {
    "font_size": 9,
    "node_size": 200,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1.2,
    "width": 1.4,
}
nx.draw_networkx(lift, pos,style="dashed", **options)
nx.draw_networkx(slope, pos, edge_color=colors,connectionstyle="arc3,rad=0.1", **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
