import sys

class Vertex:
  def __init__(self, node):
    self.id = node
    self.adjacent = {}
    self.distance = sys.maxint
    self.visited = False
    self.previous = None

  def addNeighbor(self, neighbor, weight = 0):
    self.adjacent[neighbor] = weight

  def getConnections(self):
    return self.adjacent.keys()

  def getId(self):
    return self.id

  def getWeight(self, neighbor):
    return self.adjacent[neighbor]

  def setDistance(self, distance):
    self.distance = distance

  def getDistance(self):
    return self.distance

  def setPrevious(self, previous):
    self.previous = previous

  def setVisited(self):
    self.visited = True

  def __str__(self):
    return str(self.id) + ' adjacente(s): ' + str([x.id for x in self.adjacent])

class Graph:
  def __init__(self):
    self.vertexDict = {}
    self.numVertex = 0

  def __iter__(self):
    return iter(self.vertexDict.values())

  def addVertex(self, node):
    self.numVertex = self.numVertex + 1
    newVertex = Vertex(node)
    self.vertexDict[node] = newVertex
    return newVertex

  def getVertex(self, node):
    if node in self.vertexDict:
      return self.vertexDict[node]
    else:
      return none

  def addEdge(self, fromNode, toNode, cost = 0):
    if fromNode not in self.vertexDict:
      return 'node from not in graph'
    if toNode not in self.vertexDict:
      return 'node to not in graph'

    self.vertexDict[fromNode].addNeighbor(self.vertexDict[toNode], cost)
    self.vertexDict[toNode].addNeighbor(self.vertexDict[fromNode], cost)

  def getVertices(self):
    return self.vertexDict.keys()

  def setPrevious(self, current):
    self.previous = current

  def getPrevious(self, current):
    return self.previous