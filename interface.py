from graph import Vertex as Vertex
from graph import Graph as Graph
from dijkstra import dijkstra as Dijkstra
from prim import prim as Prim
import random
import time

def generateRandomWeightedGraph(numberVertices, probability, lowerWeight, higherWeight):
	aGraph = Graph()

	for x in range(1, numberVertices):
		aGraph.addVertex(str(x))

	for aVertex in aGraph:
		for bVertex in aGraph:
			if bVertex.getId() == aVertex.getId() or bVertex.getId() in aVertex.getConnections():
				continue
			if(probability > random.randrange(0, 100)):
				aGraph.addEdge(aVertex.getId(), bVertex.getId(), random.randint(lowerWeight, higherWeight))

	return aGraph

if __name__ == '__main__':
	g1 = generateRandomWeightedGraph(200, 90, 1, 5)
	g2 = generateRandomWeightedGraph(300, 90, 1, 5)
	g3 = generateRandomWeightedGraph(400, 90, 1, 5)
	g4 = generateRandomWeightedGraph(200, 20, 1, 5)
	g5 = generateRandomWeightedGraph(300, 20, 1, 5)
	g6 = generateRandomWeightedGraph(400, 20, 1, 5)

	startTimeDijkstra = time.time()
	Dijkstra(g1, g1.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g1, g1.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Primeira Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

	startTimeDijkstra = time.time()
	Dijkstra(g2, g2.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g2, g2.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Segunda Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

	startTimeDijkstra = time.time()
	Dijkstra(g3, g3.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g3, g3.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Terceira Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

	startTimeDijkstra = time.time()
	Dijkstra(g4, g4.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g4, g4.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Quarta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

	startTimeDijkstra = time.time()
	Dijkstra(g5, g5.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g5, g5.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Quinta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

	startTimeDijkstra = time.time()
	Dijkstra(g6, g6.getVertex('1'))
	totalTimeDijkstra = time.time() - startTimeDijkstra
	startTimePrim = time.time()
	Prim(g6, g6.getVertex('1'))
	totalTimePrim = time.time() - startTimePrim
	print("----------------- Sexta Amostra -----------------\nDijkstra: %s segundos\nPrim: %s segundos\n----------------------------------------------------\n" % (totalTimeDijkstra, totalTimePrim))

