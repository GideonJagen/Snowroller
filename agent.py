from networkx.classes import graph
import numpy as np

class Agent:

	def __init__(self, parent_graph, start_node):

		self._parent_graph = parent_graph

		self._queue_position = 0
		self._queue_destination = None
		self._node = start_node # current node index
		self._edge = None # index if agent is on edge
		#self.group_size =  1 + int(4 * np.random.rand())
		#self.skill_level = np.random.rand()
		self._timer = 0.0
		#self.queue_times = np.array()

	def update(self, dt=1):
		if self._queue_position:
			self._queue_position -= self._parent_graph.get_edge_attribute(self._queue_destination, 'capacity')*dt
			if self._queue_position <= 0:
				self._parent_graph.leave_queue(self._queue_destination)
				self._queue_position = 0
				self._timer = self._parent_graph.get_edge_attribute(self._queue_destination, 'time')
				self._edge = self._queue_destination
				self._queue_destination = None
		elif self._edge:
			# wait to arrive at destination node
			self._timer -= dt
			if self._timer <= 0.0:
				_, self._node = self._parent_graph.decode_slope(self._edge)
				self._edge = None
		else:
			# fetch neighbours
			neighbours = self._parent_graph.get_neighbors(self._node)

			# select neighbour (randomly for now)
			destination = self._parent_graph.encode_slope(self._node, np.random.choice(list(neighbours.keys())))
			
			if self._parent_graph.get_edge_attribute(destination, 'lift'):
				self._queue_position = self._parent_graph.get_edge_attribute(destination, 'queue')
				self._parent_graph.enter_queue(destination)
				self._queue_destination = destination
			else:
				# set timer
				self._timer = self._parent_graph.get_edge_attribute(destination, 'time')

				# enter edge
				self._edge = destination

	def print_status(self):
		if self._edge:
			print('currently on edge ' + str(self._edge))
		else:
			print('currently at node ' + str(self._node))