import heapq

class Grafo:
    def __init__(self):
        self.arestas = {} 

    def adicionar_aresta(self, origem, destino, distancia):
        if origem not in self.arestas:
            self.arestas[origem] = []
        if destino not in self.arestas:
            self.arestas[destino] = []
        self.arestas[origem].append((destino, distancia))
        self.arestas[destino].append((origem, distancia))  

    def dijkstra(self, origem):
        # Inicializando distâncias e fila de prioridade
        distancias = {nodo: float('inf') for nodo in self.arestas}
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]
        while fila_prioridade:
            distancia_atual, no_atual = heapq.heappop(fila_prioridade)

            #Ignoramos a distancia atual se já encontramos uma distância menor
            if distancia_atual > distancias[no_atual]:
                continue

            for vizinho, peso in self.arestas[no_atual]:
                distancia = distancia_atual + peso

                # Se a nova distância calculada for menor que a distância armazenada atualmente para o nó vizinho,
                # atualizamos a distância mínima para esse nó vizinho e o adicionamos de volta na fila de prioridade
                # com a nova distância, para que ele seja processado posteriormente.
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(fila_prioridade, (distancia, vizinho))

        return distancias
