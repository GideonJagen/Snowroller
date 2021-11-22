import numpy as np

class Agent:

	def __init__(self, parent_graph, start_node):
		self.node = start_node # current node index
		self.parent_graph = parent_graph
		self.group_size =  1 + int(4 * np.random.rand())
		self.skill_level = np.random.rand()
		#self.queue_times = np.array()

	def update(dt):

		if self.edge:
			# wait to re-emerge
			self.wait_time -= dt
			if self.wait_time <= 0.0:
				self.edge = None
		else:
			# at node
			
			# fetch neighbours
			neighbours = self.parent_graph.get_neighbours(self.node)

			# select neighbour
			for n in neighbours.keys():


			# enter edge