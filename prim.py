from graph import Vertex as Vertex
from graph import Graph as Graph
from pythonds.graphs import PriorityQueue
import sys

def prim(aGraph, start):
    pq = PriorityQueue()
    for vertex in aGraph:
        vertex.setDistance(sys.maxsize)
        vertex.setPrevious(None)
    start.setDistance(0)
    pq.buildHeap([(vertex.getDistance(), vertex) for vertex in aGraph])
    while not pq.isEmpty():
        currentVertex = pq.delMin()
        for nextVertex in currentVertex.getConnections():
          newCost = currentVertex.getWeight(nextVertex)
          if nextVertex in pq and newCost < nextVertex.getDistance():
              nextVertex.setPrevious(currentVertex)
              nextVertex.setDistance(newCost)
              pq.decreaseKey(nextVertex,newCost)
