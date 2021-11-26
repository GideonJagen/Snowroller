import numpy as np
from agent import Agent
from graph import Graph
from matplotlib import pyplot as plt

def main():

    graph = Graph()
    agents = []
    for agent in range(1000):
        agents.append(Agent(graph, 1))
        Agent(graph, 1)

    queue12 = []
    queue14 = []
    queue34 = []
    queue54 = []
    for time in range(200):
        print(time)
        for agent in agents:
            agent.update()
        queues = graph.get_queues()
        queue12.append(queues[0])
        queue14.append(queues[1])
        queue34.append(queues[2])
        queue54.append(queues[3])

    fig, axs = plt.subplots(2, 2, sharex='all', sharey='all')
    axs[0, 0].plot(queue12)
    axs[0, 0].set_title("Lift 1 -> 2")
    axs[0, 1].plot(queue14)
    axs[0, 1].set_title("Lift 1 -> 4")
    axs[1, 0].plot(queue34)
    axs[1, 0].set_title("Lift 3 -> 4")
    axs[1, 1].plot(queue54)
    axs[1, 1].set_title("Lift 5 -> 4")
    fig.text(0.5, 0.04, 'Time (min)', ha='center')
    fig.text(0.04, 0.5, 'Agents in Queue', va='center', rotation='vertical')
    plt.show()

    


if __name__ == '__main__':
    main()