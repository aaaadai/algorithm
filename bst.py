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

	def delete(self, v):
		if self.root == None:
			return False
		elif v < self.root.value:
			return self._delete(self.root, self.root.l, v)
		elif v > self.root.value:
			return self._delete(self.root, self.root.r, v)
		elif v == self.root.value:
			return self._delete(None, self.root, v)

	def _delete(self, p, n, v):
		if n == None:
			return False
		elif v < n.value:
			return self._delete(n, n.l, v)
		elif v > n.value:
			return self._delete(n, n.r, v)
		elif v == n.value:
			# 要删除的node是leaf node
			if n.l == None and n.r == None:
				if p == None:
					self.root = None
				elif p.l == n:
					p.l = None
				elif p.r == n:
					p.r = None
				print('case 1')
				return True
			# 要删除的node只有一个child node
			elif n.l == None and n.r != None:
				if p == None:
					self.root = n.r
				elif p.l == n:
					p.l = n.r
				elif p.r == n:
					p.r = n.r
				print('case 2')
				return True
			elif n.l != None and n.r == None:
				if p == None:
					self.root = n.l
				elif p.l == n:
					p.l = n.l
				elif p.r == n:
					p.r = n.l
				print('case 2')
				return True
			# 要删除的node有两个child node，默认用left child里面的最大值替换
			elif (n.l != None) and (n.r != None):
				current_node = n.l
				previous_node = None
				while current_node.r != None:
					previous_node = current_node
					current_node = current_node.r
				if previous_node != None:
					previous_node.r = current_node.l
				print(current_node.value)
				if current_node != n.l:
					current_node.l = n.l
				else:
					current_node.l = None
				current_node.r = n.r
				if p == None:
					self.root = current_node
				elif p.l == n:
					p.l = current_node
				elif p.r == n:
					p.r = current_node
				return True



if __name__ == '__main__':
	#exampleList = [random.randint(0, 100) for a in range(0, 20)]
	exampleList = [22, 4, 69, 12, 2, 73, 54, 41, 39, 49, 89, 92, 50, 64, 20, 34, 17, 27, 94, 11]
	t = Tree()
#	for num in exampleList:
#		t.insert(num)
#	print(exampleList)
#	t.preorder()
#	t.postorder()
	t.insert(8)
	t.insert(7)
	t.insert(2)
	t.insert(1)
	t.insert(4)
	t.insert(3)
	t.insert(5)
	t.insert(6)
	t.inorder()


	t.delete(2)
	t.inorder()



