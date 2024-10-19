import sys

def analisar_uso_memoria(grafo, caminhoes, entregas):
    print("------INICIO DA ANALISE DE USO DE MEMORIA:")
    print(f"Tamanho da estrutura de dados do grafo: {sys.getsizeof(grafo)} bytes")
    print(f"Tamanho da estrutura de dados dos caminhões: {sys.getsizeof(caminhoes)} bytes")
    print(f"Tamanho da estrutura de dados das entregas: {sys.getsizeof(entregas)} bytes")
    print("------FIM DA ANALISE DE USO DE MEMORIA: \n")

