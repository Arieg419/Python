class Node(object):

	def __init__(self, data, parentNode):
		self.data = data;
		self.parentNode = parentNode;
		self.rightChild = None;
		self.leftChild = None;
		self.balance = 0;

	def insert(self, data, parentNode):
		#must go to left
		if data < self.data:
			if not self.leftChild:
				self.leftChild = Node(data, parentNode);
			else:
				self.leftChild.insert(data, parentNode);
		#we go to the right
		else:
			if not self.rightChild:
				self.rightChild = Node(data, parentNode);
			else:
				self.rightChild.insert(data, parentNode);

		return parentNode;
	
	def traverseInOrder(self):
		if self.leftChild:
			self.leftChild.traverseInOrder();

		print(self.data);

		if self.rightChild:
			self.rightChild.traverseInOrder();

	def getMax(self):
		if not self.rightChild:
			return self.data;
		else:
			self.rightChild.getMax();

	def getMin(self):
		if not self.leftChild:
			return self.data;
		else:
			self.leftChild.getMin();

	
