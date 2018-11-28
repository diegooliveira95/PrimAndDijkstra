from graph import Vertex as Vertex
from graph import Graph as Graph
import heapq

def shortest(v, path):
    if v.previous:
        path.append(v.previous.getId())
        shortest(v.previous, path)
    return

def dijkstra(aGraph, start): 
    start.setDistance(0)

    unvisitedQueue = [(vertex.getDistance(),vertex) for vertex in aGraph]
    heapq.heapify(unvisitedQueue)

    while len(unvisitedQueue):
        aVertex = heapq.heappop(unvisitedQueue)
        current = aVertex[1]
        current.setVisited()

        for next in current.adjacent:
            if next.visited:
                continue
            newDistance = current.getDistance() + current.getWeight(next)
            
            if newDistance < next.getDistance():
                next.setDistance(newDistance)
                next.setPrevious(current)

        while len(unvisitedQueue):
            heapq.heappop(unvisitedQueue)
        unvisitedQueue = [(vertex.getDistance(),vertex) for vertex in aGraph if not vertex.visited]
        heapq.heapify(unvisitedQueue)
