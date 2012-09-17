from graph import *

class Network:
  def __init__(self, label='default', data={}):
    self.graphs=[]
    self.label=label
    self.data=data

  def load(self, graph):
    self.graphs.append(graph)

  # Return a list of Nodes sorted by time
  def buildTimeIndex(self, graphs):
    temporal = []
    for g in graphs:
      if g.data['type'] is 'temporal':
        temporal.append(g)
    temporal.sort(lambda a,b: a.data['time']-b.data['time'])
    return temporal

  def unifyEntities(self, graphs):
    entities = {}
    for g in graphs:
      if g.data['type'] is not 'temporal': continue
      nodes = g.getAllNodes()
      for node in nodes:
        if node not in entities: entities[node] = node

    return entities

  def propagate(self, time=0, participants=[]):
    current = Graph(data={'type': 'temporal', 'time': time})
    for p in participants: current.node(Node(p))
    #self.graphs.append(current)

    timeSortedList = self.buildTimeIndex(self.graphs)
    #print timeSortedList[0].data['time'], timeSortedList[-1].data['time']

    entityIndex = self.unifyEntities(self.graphs)

    propagationNet = Graph()
    for t in timeSortedList: propagationNet.node(t)
    for e in dict.keys(entityIndex): propagationNet.node(e)

    ec = 0
    for t in timeSortedList:
      nodes = t.getAllNodes()
      for n in nodes:
        ref = entityIndex[n]
        propagationNet.edge(Edge(t, ref))
        propagationNet.edge(Edge(ref, t))
        ec += 2

    print ec, 'edges created'

  def printStats(self):
    times = []
    for graph in self.graphs:
      if 'time' not in graph.data: continue
      times.append(graph.data['time'])

    times.sort()
    #print times[0], times[len(times)-1]

    print 'Aggregate Network contains', len(self.graphs), 'graphs.'
