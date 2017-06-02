import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import heapq
from graph import *


class Dijkstra():
	"""
	Objeto calcula el camino minimo a mediante el algoritmo de dijkstra
	utilizando un grafo de aristas con sentido y con peso.
	"""

	def __init__(self, grafo):
		self.grafo = grafo

	def getShortestPath(self, src, dst):
		"""
			Recibe un vertice de origen y uno de destino.
			Devuelve una lista con los nodos que se deben recorrer para llegar
			desde source hasta dest con minima distancia y el valor de dicha distancia.
		"""
		colaP = [] 

		padres, visitados, distancias = self.getListasIniciadas()

		distancias[src] = 0
		heapq.heappush(colaP, src)


		print(float(self.grafo.obtener_peso("0", "1")))


		#Mientras que la cola de prioridad no este vacia
		while (len(colaP) > 0):
			
			vertice = heapq.heappop(colaP) #devuelve el minimo elemento
			visitados[vertice] = True
			
			for vertVecino in self.grafo.obtener_conocidos(str(vertice)):

				vecino = int(vertVecino); 

				pesoEntreEllos = float(self.grafo.obtener_peso(str(vertice), vertVecino))
				if( (not visitados[vecino]) and (distancias[vecino] > (distancias[vertice] + pesoEntreEllos) ) ):
					distancias[vecino] = distancias[vertice] + pesoEntreEllos
					padres[vecino] = vertice
					heapq.heappush(colaP, vecino)

		return self.calculoDeCaminoMinimo(src, dst, padres), distancias[dst]

	def calculoDeCaminoMinimo(self, src, dst, padres):
		"""
		Calculo el camino minimo entre 2 vertices de atras para adelante
		"""
		path = []
		step = dst

		if(padres[step] is None):
			return None

		path.append(step)
		while (padres[step] != src):
			step = padres[step]
			path.append(step);
		path.append(src)	

		#Se da vuelta la lista para que vaya src-dest y no dest-src
		path = list(reversed(path))	

		return path


	def getListasIniciadas(self):

		cantVert = len(self.grafo)
		padres = [None] * cantVert
		visitados = [False] * cantVert
		distancias = [VALOR_INALCANZABLE] * cantVert

		return padres, visitados, distancias	