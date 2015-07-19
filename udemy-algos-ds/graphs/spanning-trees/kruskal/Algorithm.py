#can have a running time of O(nlogn) with mergesort or quicksort
#union find data structure --> O(logV)
#worst case running time is O(ElogE)
#pick smallest edge, check for cycle, skip if cycle detected
from DisjointSet import DisjointSet;

class Algorithm(object):

	def constructSpanningTree(self, vertexList, edgeList):
		disjointSet = DisjointSet(vertexList);
		spanningTree = [];

		edgeList.sort(); #O(nlogn)

		for edge in edgeList:
			u = edge.startVertex;
			v = edge.targetVertex;
			
			if disjointSet.find(u.parentNode) is not disjointSet.find(v.parentNode):
				spanningTree.append(edge);
				disjointSet.union(u.parentNode, v.parentNode);

		for edge in spanningTree:
			print(edge.startVertex.name, "-", edge.targetVertex.name);
