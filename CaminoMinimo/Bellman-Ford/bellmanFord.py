import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from graph import *

class BellmanFord():
    """
        Algoritmo de Bellman-Ford para encontrar el camino minimo
        entre dos vertices de un grafo dirigido, ponderado y sin
        ciclos negativos.
    """
    def __init__(self, graph):
        self.graph = graph

    def bellmanFord(self, source):
        """
            Se realiza el algoritmo de Bellman-Ford en si, que devuelve una
            lista con todas las distancias desde source hasta cada vertice y
            quien es el padre de cada uno.
        """
        #Se inicializan todas las distancias en infinito y los anteriores en None
        distance = [VALOR_INALCANZABLE]*len(self.graph)
        previous = [None]*len(self.graph)
        #Se setea la distancia a si mismo como 0
        distance[int(source)] = 0

        #Se relajan las aristas
        for i in xrange(len(self.graph)):
            for vertex in self.graph.vertices.keys():
                #Para cada arista en E[G]
                vertexAdj = self.graph.obtener_conocidos(vertex) #Vecinos de vertex
                for adjacent in vertexAdj:
                    edgeWeight = float(self.graph.obtener_peso(vertex, adjacent))
                    u = int(vertex)
                    v = int(adjacent)
                    #Si hay un camino mas corto, se actualiza
                    if distance[v] > distance[u] + edgeWeight:
                        distance[v] = distance[u] + edgeWeight #nuevo peso
                        previous[v] = u #nuevo padre

        return (distance, previous)

    def getShortestPath(self, source, dest):
        """
            Recibe un vertice de origen y uno de destino.
            Devuelve una lista con los nodos que se deben recorrer para llegar
            desde source hasta dest con minima distancia y el valor de dicha distancia.
        """
        #Se hace bellman ford y se obtienen las listas iniciales
        (distance, previous) = self.bellmanFord(source)

        #El camino empieza con dest
        path = [dest]
        parent = None #Padre de cada vertice
        vertex = dest #Vertice que va cambiando (para atras)
        print (previous)
        while (parent != None):
            parent = previous[int(dest)]
            path.append(str(parent)) #Se guarda el vertice
        path.append(source)
        #Se da vuelta la lista para que vaya src-dest y no dest-src
        path = list(reversed(path))
        #Peso del camino minimo
        weight = distance[int(dest)]

        return (path, weight)
