import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from graph import *


INF  = 1000000000.0

class floydWarshall():

    """Algoritmo de Bellman-Ford para encontrar el camino minimo
    entre todos los pares de vertices de un grafo dirigido"""
    def __init__(self, grafo):
        self.grafo = grafo
        self.dist = grafo.get_vertices()

    """Algoritmo de floydWarshall.
    Luego de terminado el algoritmo el diccionario de distancias debe contener
    las menores distancias entra cada par de vertices.
    Es inicializado como la matriz de adyacencia del grafo dado por parametro."""

    def floydWarshall(self):
        numV = len(self.grafo)

        for k in xrange(numV):
            for i in xrange(1,numV):
                for j in xrange(2,numV):

                    auxK = str(k)
                    auxI = str(i)
                    auxJ = str(j)

                    if(not self.dist[auxI].has_key(auxK) or not self.dist[auxK].has_key(auxJ) or not self.dist[auxI].has_key(auxJ) ):
                        continue

                    distAux = float(self.dist[auxI][auxK]) + float(self.dist[auxK][auxJ])

                    if(float(self.dist[auxI][auxJ]) > distAux ):
                        self.dist[auxI][auxJ] = str(distAux)



    def calculoDeCaminoMinimo(self, src, dst):
        return self.dist[src][dst]
