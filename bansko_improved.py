import networkx as nx
import matplotlib.pyplot as plt

lift = nx.DiGraph()     #weight, tid, people/tid, allt i min
lift.add_edge(1, 2, lift = True, queue = 0, time=10, pph=33.3)    #bansko
lift.add_edge(3, 2, lift = True, queue = 0, time=4, pph=32.75)   #chalin valog
lift.add_edge(2, 4, lift = True, queue = 0, time=11, pph=33.3)   #bansko
lift.add_edge(4, 5, lift = True, queue = 0, time=6.3, pph=33.33)   #Banderitza 1
lift.add_edge(4, 6, lift = True, queue = 0, time=2.5, pph=50)   #Kolarski
lift.add_edge(7, 6, lift = True, queue = 0, time=7.2, pph=15.9)   #stara kotva
lift.add_edge(8, 6, lift = True, queue = 0, time=6.5, pph=15.9)   #detska kotva
lift.add_edge(8, 9, lift = True, queue = 0, time=7, pph=33.3)   #todorka
lift.add_edge(5, 10, lift = True, queue = 0, time=3.5, pph=33.33)  #Banderitza 2
lift.add_edge(8, 11, lift = True, queue = 0, time=7.5, pph=33.33)  #shiligarnik
lift.add_edge(11, 10, lift = True, queue = 0, time=5.5, pph=36.67) #Plato
lift.add_edge(12, 11, lift = True, queue = 0, time=9.5, pph=32.33) #mosta

#lift.add_edge(1, 11, lift = True, queue = 0, time=9.5, pph=32.33) #miproved lift
#kan också förbättra genom att dubbla capaciteten av lift 1-2
lift.add_edge(13, 12, lift = True, queue = 0, time=9.5, pph=32.33) #miproved lift


slope = nx.DiGraph()
slope.add_edge(2, 3,color='r', lift = False, difficulty = 0.75, time = 1)
slope.add_edge(2, 3,color='b', lift = False, difficulty = 0.5, time = 3)    # 2 Backar
slope.add_edge(4, 1,color='b', lift = False, difficulty = 0.5, time = 20)
slope.add_edge(4, 3,color='b', lift = False, difficulty = 0.5, time = 14)
slope.add_edge(3, 1,color='b', lift = False, difficulty = 0.5, time = 6)
slope.add_edge(5, 4,color='k', lift = False, difficulty = 1, time = 3)
slope.add_edge(6, 7,color='r', lift = False, difficulty = 0.75, time = 3)
slope.add_edge(6, 8,color='b', lift = False, difficulty = 0.5, time = 7)
slope.add_edge(6, 8,color='r', lift = False, difficulty = 0.75, time = 4)    #2 stycken
slope.add_edge(8, 7,color='b', lift = False, difficulty = 0.5, time = 6)
slope.add_edge(7, 4,color='b', lift = False, difficulty = 0.5, time = 8)
slope.add_edge(8, 12,color='b', lift = False, difficulty = 0.5, time = 6)
slope.add_edge(9, 8,color='r', lift = False, difficulty = 0.75, time = 6)
slope.add_edge(9, 5,color='r', lift = False, difficulty = 0.75, time = 4)
slope.add_edge(5, 6,color='r', lift = False, difficulty = 0.75, time = 3)
slope.add_edge(10, 9,color='r', lift = False, difficulty = 0.75, time = 3)
slope.add_edge(10, 5,color='r', lift = False, difficulty = 0.75, time = 10)
slope.add_edge(10, 11,color='b', lift = False, difficulty = 0.5, time = 14)
slope.add_edge(9, 11,color='b', lift = False, difficulty = 0.5, time = 8)
slope.add_edge(11, 8,color='b', lift = False, difficulty = 0.5, time = 8)
slope.add_edge(11, 12,color='b', lift = False, difficulty = 0.5, time = 7)
slope.add_edge(12, 2,color='g', lift = False, difficulty = 0.25, time = 4)


# explicitly set positions
pos = {1: (0.9,0),2:(1.3,8),3:(1.3,4),4:(2.15,11),5:(1.87,22),6:(1.8,17),7:(1.75,12),8:(1.55,14),9:(1.85,30),10:(1.9,36),11:(1.4,27),12:(1.3,13),13:(0.8,8)}
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
