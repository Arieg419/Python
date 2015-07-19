#lazy implementation - add new neighbor edge without deleting content
#eager implementation - keep updating heap if distance from a vertex to MST has change
#average running time is O(ElogE), worst case is O(ElogV)
import heapq;

class Algorithm(object):

	def __init__(self, unvisitedList):
		self.unvisitedList = unvisitedList;
		self.spanningTree = [];
		self.edgeHeap = [];
		self.fullCost = 0;

	def calculateSpanningTree(self, vertex):
		self.unvisitedList.remove(vertex);

		while self.unvisitedList:
			for edge in vertex.adjacenciesList:
				if edge.targetVertex in self.unvisitedList:
					heapq.heappush(self.edgeHeap, edge);

			minEdge = heapq.heappop(self.edgeHeap);

			self.spanningTree.append(minEdge);
			print("Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name, minEdge.targetVertex.name));
			self.fullCost += minEdge.weight;

			vertex = minEdge.targetVertex;
			self.unvisitedList.remove(vertex)

	def getSpanningTree(self):
		return self.spanningTree;
