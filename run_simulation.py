import numpy as np
from agent import Agent
from graph import Graph
from matplotlib import pyplot as plt

def main():

    graph = Graph(bansko=True)
    agents = []
    for agent in range(4000):
        agents.append(Agent(graph, 1))

    queue12 = []
    queue32 = []
    queue24 = []
    queue45 = []
    queue46 = []
    queue76 = []
    queue86 = []
    queue89 = []
    queue510 = []
    queue811 = []
    queue1110 = []
    queue1211 = []
    queue111 = []
    for time in range(480):
        #print(time)
        for agent in agents:
            agent.update()
        queues = graph.get_queues()
        capacities = graph.get_capacities()
        queue12.append(queues[0]/capacities[0])
        queue32.append(queues[1]/capacities[1])
        queue24.append(queues[2]/capacities[2])
        queue45.append(queues[3]/capacities[3])
        queue46.append(queues[4]/capacities[4])
        queue76.append(queues[5]/capacities[5])
        queue86.append(queues[6]/capacities[6])
        queue89.append(queues[7]/capacities[7])
        queue510.append(queues[8]/capacities[8])
        queue811.append(queues[9]/capacities[9])
        queue1110.append(queues[10]/capacities[10])
        queue1211.append(queues[11]/capacities[11])
        queue111.append(queues[12]/capacities[12])

    fig, axs = plt.subplots(7, 2, sharex='all', sharey='all')
    axs[0,0].set_title('Queue 1 -> 2')
    axs[0, 0].plot(queue12)
    axs[0,1].set_title('Queue 3 -> 2')
    axs[0, 1].plot(queue32)
    axs[1,0].set_title('Queue 2 -> 4')
    axs[1, 0].plot(queue24)
    axs[1,1].set_title('Queue 4 -> 5')
    axs[1, 1].plot(queue45)
    axs[2,0].set_title('Queue 4 -> 6')
    axs[2, 0].plot(queue46)
    axs[2,1].set_title('Queue 7 -> 6')
    axs[2, 1].plot(queue76)
    axs[3,0].set_title('Queue 8 -> 6')
    axs[3, 0].plot(queue86)
    axs[3,1].set_title('Queue 8 -> 9')
    axs[3, 1].plot(queue89)
    axs[4,0].set_title('Queue 5 -> 10')
    axs[4, 0].plot(queue510)
    axs[4,1].set_title('Queue 8 -> 11')
    axs[4, 1].plot(queue811)
    axs[5, 0].set_title('Queue 11 -> 10')
    axs[5, 0].plot(queue1110)
    axs[5,1].set_title('Queue 12 -> 11')
    axs[5, 1].plot(queue1211)
    axs[6,0].set_title('Queue 1 -> 11')
    axs[6, 0].plot(queue111)

    fig.text(0.5, 0.04, 'Time (min)', ha='center')
    fig.text(0.04, 0.5, 'Agents in Queue', va='center', rotation='vertical')
    plt.show()

    


if __name__ == '__main__':
    main()