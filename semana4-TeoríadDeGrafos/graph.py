class Graph:
  def __init__(self):
    self.Vertices = []
    self.label2v = dict()
    self.G = []

  def node(self, label):
    self.label2v[label] = len(self.Vertices)
    self.Vertices.append(label)
    self.G.append([])

  def nodes(self, labels):
    for label in labels:
      self.node(label)

  def edge(self, u, v):
    u = self.label2v[u]
    v = self.label2v[v]

    self.G[u].append(v)

  def edges(self, u, vs):
    for v in vs:
      self.edge(u, v)

  def Dot(self):
    graph = gv.Digraph("X")
    n = len(self.G)
    for u in range(n):
      graph.node(str(u), str(self.Vertices[u]))

    for u in range(n):
      for v in self.G[u]:
        graph.edge(str(u), str(v))

    return graph