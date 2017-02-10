import random

class Node(object):
	def __init__(self, v):
		self.value = v
		self.l = None
		self.r = None

class Tree(object):
	def __init__(self):
		self.root = None

	def insert(self, v):
		if self.root == None:
			self.root = Node(v)
		else:
			self._insert(self.root, v)

	def _insert(self, n, v):
		if v < n.value and n.l == None:
			n.l = Node(v)
		elif v >= n.value and n.r == None:
			n.r = Node(v)
		elif v < n.value:
			self._insert(n.l, v)
		elif v >= n.value:
			self._insert(n.r, v)

	def find(self,v):
		if self.root == None:
			return False
		else:
			return self.root.find(v)

	def _find(self, n, v):
		if v == n.value:
			return True
		elif v < n.value and n.l != None:
			return self._find(n.l, v)
		elif v > n.value and n.r != None:
			return self._find(n.r, v)
		return False

	def inorder(self):
		if self.root:
			if self.root.l:
				self._inorder(self.root.l)
			print(self.root.value)
			if self.root.r:
				self._inorder(self.root.r)
		else:
			print('Empty Tree')

	def _inorder(self, n):
		if n.l:
			self._inorder(n.l)
		print(n.value)
		if n.r:
			self._inorder(n.r)

	def preorder(self):
		if self.root:
			print(self.root.value)
			if self.root.l:
				self._preorder(self.root.l)
			if self.root.r:
				self._preorder(self.root.r)
		else:
			print('Empty Tree')

	def _preorder(self, n):
		print(n.value)
		if n.l:
			self._preorder(n.l)
		if n.r:
			self._preorder(n.r)

	def postorder(self):
		if self.root:
			if self.root.l:
				self._postorder(self.root.l)
			if self.root.r:
				self._postorder(self.root.r)
			print(self.root.value)
		else:
			print('Empty Tree')

	def _postorder(self, n):
		if n.l:
			self._postorder(n.l)
		if n.r:
			self._postorder(n.r)
		print(n.value)

#	def delete(self, v):
#		if self.root == None:
#			return False
#		elif v < self.root.value:
#			return self._delete(self.root.l, v)
#		elif v > self.root.value:
#			return self._delete(self.root.r, v)
#		elif v == self.root.value:
#			return self._delete(self.root, v)#

#	def _delete(self, n, v):
#		if n == None:
#			return False
#		elif v < n.value:
#			return self._delete(n.l, v)
#		elif v > n.value:
#			return self._delete(n.r, v)
#		else v == n.value:
#			if n.l == None and n.r == None:


if __name__ == '__main__':
	exampleList = [random.randint(0, 100) for a in range(0, 20)]
	t = Tree()
	for num in exampleList:
		t.insert(num)
	print(exampleList)
	t.inorder()
#	t.preorder()
#	t.postorder()


