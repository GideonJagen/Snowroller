from networkx.classes import graph
from operator import itemgetter
import numpy as np

class Agent:

	def __init__(self, parent_graph, start_node):
		self._parent_graph = parent_graph

		self._queue_position = 0
		self._queue_destination = None
		self._node = start_node # current node index
		self._edge = None # index if agent is on edge
		#self.group_size =  1 + int(4 * np.random.rand())
		self._skill_level = 0.25 + np.random.rand() * 0.75
		self._timer = 0.0
		#self.queue_times = np.array()
		self._scoring = self._score_edges()

	def _score_edges(self):
		scoring = {}

		# assign score to slopes
		for edge in self._parent_graph.graph.edges():
			attributes = self._parent_graph.graph[edge[0]][edge[1]]
			
			if attributes['lift'] == False:
				# 1. if perfect match, 0.05 if complete mismatch
				score = np.exp(-3*abs(attributes['difficulty'] - self._skill_level))
				# add random perturbation to score to represent subjective preference?
				scoring[self._parent_graph.encode_slope(edge[0], edge[1])] = score

		# lifts inherit the highest slope score they lead to
		for edge in self._parent_graph.graph.edges():
			attributes = self._parent_graph.graph[edge[0]][edge[1]]
			
			if attributes['lift'] == True:
				highest_score = 0.

				# get slopes that this lift leads to
				for out in self._parent_graph.graph.out_edges(edge[1]):
					out_attr = self._parent_graph.graph[out[0]][out[1]]
					if out_attr['lift'] == False: # make sure that out edge actually is a slope
						slope_score = scoring[self._parent_graph.encode_slope(out[0], out[1])]
						highest_score = max(highest_score, slope_score)

				scoring[self._parent_graph.encode_slope(edge[0], edge[1])] = highest_score

		return scoring


		self._parent_graph.component_population[start_node] += 1

	def update(self, dt=1):
		if self._queue_position:
			self._queue_position -= self._parent_graph.get_edge_attribute(self._queue_destination, 'capacity')*dt
			if self._queue_position <= 0:
				self._parent_graph.leave_queue(self._queue_destination)
				self._queue_position = 0
				self._timer = self._parent_graph.get_edge_attribute(self._queue_destination, 'time')
				self._edge = self._queue_destination
				self._parent_graph.reposition_agent(self._node, self._edge)
				self._queue_destination = None
		elif self._edge:
			# wait to arrive at destination node
			self._timer -= dt
			if self._timer <= 0.0:
				_, self._node = self._parent_graph.decode_slope(self._edge)
				self._parent_graph.reposition_agent(self._edge, self._node)
				self._edge = None
		else:
			# fetch neighbours
			neighbours = self._parent_graph.get_neighbors(self._node)

			# select destination edge based on scores
			neighbour_edges = list(map(lambda n: self._parent_graph.encode_slope(self._node, n), neighbours))
			neighbour_scores = itemgetter(*neighbour_edges)(self._scoring)
			if type(neighbour_scores)==np.float64: neighbour_scores = [neighbour_scores]
			destination = np.random.choice(neighbour_edges, p=neighbour_scores/np.sum(neighbour_scores))

			# randomly select destination
			#destination = self._parent_graph.encode_slope(self._node, np.random.choice(list(neighbours.keys())))
			
			if self._parent_graph.get_edge_attribute(destination, 'lift'):
				self._queue_position = self._parent_graph.get_edge_attribute(destination, 'queue')
				self._parent_graph.enter_queue(destination)
				self._queue_destination = destination
			else:
				# set timer
				self._timer = self._parent_graph.get_edge_attribute(destination, 'time')

				# enter edge
				self._edge = destination
				self._parent_graph.reposition_agent(self._node, self._edge)

	def print_status(self):
		if self._edge:
			print('currently on edge ' + str(self._edge))
		else:
			print('currently at node ' + str(self._node))