#running time = O(V + E)
#not as efficient as DFS


def bfs(startNode):
	stack = [];
	startNode.visited = True;
	stack.append(startNode);

	while stack:
		actualNode = stack.pop();
		print("%s ->" % actualNode.name);

		for n in actualNode.adjacenciesList:
			if not n.visited:
				n.visited = True;
				stack.append(n);
