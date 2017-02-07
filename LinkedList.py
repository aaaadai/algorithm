class Node (object):
	def __init__ (self, d, n = None):
		self.data = d
		self.next_node = n

	def get_data(self):
		return self.data

	def set_data(self, d):
		self.data = d

	def get_next(self):
		return self.next_node

	def set_next(self, n):
		self.next_node = n

class LinkList (object):
	def __init__ (self, r = None):
		self.root = r
			if r:
				self.size = 1
			else: 
				self.size = 0

	def get_size(self):
		return self.size

	def add(self, d):
		new_node = Node(d, self.root)
		self.root = new_node
		self.siez += 1

	def remove(self, d):
		this_node = self.root
		prev_node = None
		while this_node:
			if this_node.get_data == d:
				if prev_node:
					prev_node.set_next(this_node.get_next())
				else:
					self.root = this_node.get_next()
					return True
			else:
				prev_node = this_node
				this_node = this_node.get_next()
			return False

	def find (self, d):
		this_node = self.root
		while this_node:
			if this_node.get_data() == d:
				return d
			else:
				this_node = this_node.get_next()
		return None






