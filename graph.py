class Vertex (object):
	def __init__ (self, n):
		self.name = n
		self.neighbors = []
		self.distance = 99999
		self.color = 'black'

	def add_neighbor (self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph (object):
	vertices = {}

	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_neighbor(v)
			self.vertices[v].add_neighbor(u)
			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].distance))

	def bfs(self, vert):
		q = []
		vert.distance = 0
		vert.color = 'red'

		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)

		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'
			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)
					if node_v.distance > node_u.distance:
						node_v.distance = node_u.distance + 1


if __name__ == '__main__':
	g = Graph()
	# print(str(len(g.vertices)))
	a = Vertex('A')
	g.add_vertex(a)
	g.add_vertex(Vertex('B'))
	for i in range(ord('A'), ord('K')):
		g.add_vertex(Vertex(chr(i)))	

	edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:])	

	g.bfs(a)
	g.print_graph()	
	
		