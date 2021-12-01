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
    for time in range(480):
        #print(time)
        for agent in agents:
            agent.update()
        queues = graph.get_queues()
        queue12.append(queues[0])
        queue32.append(queues[1])
        queue24.append(queues[2])
        queue45.append(queues[3])
        queue46.append(queues[4])
        queue76.append(queues[5])
        queue86.append(queues[6])
        queue89.append(queues[7])
        queue510.append(queues[8])
        queue811.append(queues[9])
        queue1110.append(queues[10])
        queue1211.append(queues[11])

    fig, axs = plt.subplots(6, 2, sharex='all', sharey='all')
    axs[0, 0].plot(queue12)
    axs[0, 1].plot(queue32)
    axs[1, 0].plot(queue24)
    axs[1, 1].plot(queue45)
    axs[2, 0].plot(queue46)
    axs[2, 1].plot(queue76)
    axs[3, 0].plot(queue86)
    axs[3, 1].plot(queue89)
    axs[4, 0].plot(queue510)
    axs[4, 1].plot(queue811)
    axs[5, 0].plot(queue1110)
    axs[5, 1].plot(queue1211)

    fig.text(0.5, 0.04, 'Time (min)', ha='center')
    fig.text(0.04, 0.5, 'Agents in Queue', va='center', rotation='vertical')
    plt.show()

    


if __name__ == '__main__':
    main()