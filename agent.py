import numpy as np

class Agent:

	def __init__(self, parent_graph, start_node):
		self._node = start_node # current node index
		self._edge = None # index if agent is on edge
		self._parent_graph = parent_graph
		#self.group_size =  1 + int(4 * np.random.rand())
		#self.skill_level = np.random.rand()
		self._timer = 0.0
		#self.queue_times = np.array()

	def update(self, dt=1):

		if self._edge:
			# wait to arrive at destination node
			self._timer -= dt
			if self._timer <= 0.0:
				_, self._node = self._parent_graph.decode_slope(self._edge)
				self._edge = None
		else:
			# fetch neighbours
			neighbours = self._parent_graph.get_neighbors(self._node)

			# select neighbour (randomly for now)
			destination = np.random.choice(list(neighbours.keys()))

			# set timer
			self._timer = np.random.uniform(1, 3)

			# enter edge
			self._edge = self._parent_graph.encode_slope(self._node, destination)

	def print_status(self):
		if self._edge:
			print('currently on edge ' + str(self._edge))
		else:
			print('currently at node ' + str(self._node))