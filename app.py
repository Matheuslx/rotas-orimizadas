from domain.grafo import Grafo
from domain.caminhao import Caminhao
from domain.entrega import Entrega
from service.alocar_caminhoes_service import alocar_caminhoes
from service.analisar_uso_memoria import analisar_uso_memoria;
import time

def executar_poucas_entregas_rotas_curtas():
    tempo_inicial = time.time()

    print("Cenário 1: Poucas entregas e rotas curtas")
    # Criando os centros de distribuições e a distancia em KM entre os destinos utilizando grafos
    grafo = Grafo()
    grafo.adicionar_aresta("Belém", "Fortaleza", 1515)
    grafo.adicionar_aresta("Belém", "Maringá", 2953)

    grafo.adicionar_aresta("Recife", "Fortaleza", 777)
    grafo.adicionar_aresta("Recife", "Maringá", 3057)

    grafo.adicionar_aresta("São Paulo", "Fortaleza", 2898)  
    grafo.adicionar_aresta("São Paulo", "Maringá", 647)  

    grafo.adicionar_aresta("Curitiba", "Fortaleza", 3469) 
    grafo.adicionar_aresta("Curitiba", "Maringá", 424)      

    caminhoes = [Caminhao(capacidade=150, limite_horas=12), Caminhao(capacidade=300, limite_horas=15)]
    
    # Adicionando prazos em dias para as entregas
    entregas = [
        Entrega("Fortaleza", peso=100, prazo_dias=1), 
        Entrega("Maringá", peso=150, prazo_dias=3)
    ]

    print("Entregas a serem realizadas:\n")
    for entrega in entregas:
        print(f"Destino: {entrega.destino}, Peso: {entrega.peso}kg, Prazo: {entrega.prazo_dias} dias")
    print("\n")

    alocar_caminhoes(grafo, caminhoes, entregas)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    print(f"\n Tempo de execução da função: {tempo_execucao:.4f} segundos \n")
    analisar_uso_memoria(grafo, caminhoes, entregas)

def executar_muitas_entregas_rotas_longas():
    tempo_inicial = time.time()

    print("\nCenário 2: Muitas entregas e rotas mais longas")

    # Criando os centros de distribuições e a distancia em KM entre os destinos utilizando grafos
    grafo = Grafo()
    grafo.adicionar_aresta("Belém", "Natal", 2020)          
    grafo.adicionar_aresta("Belém", "Belo Horizonte", 2750) 
    grafo.adicionar_aresta("Belém", "Florianópolis", 3541)   
    grafo.adicionar_aresta("Belém", "Rio de Janeiro", 3177)  
    grafo.adicionar_aresta("Belém", "Salvador", 2064)        

    grafo.adicionar_aresta("Recife", "Natal", 286)          
    grafo.adicionar_aresta("Recife", "Belo Horizonte", 2111) 
    grafo.adicionar_aresta("Recife", "Florianópolis", 3354)  
    grafo.adicionar_aresta("Recife", "Rio de Janeiro", 2308)  
    grafo.adicionar_aresta("Recife", "Salvador", 806)        

    grafo.adicionar_aresta("São Paulo", "Natal", 2883)        
    grafo.adicionar_aresta("São Paulo", "Belo Horizonte", 571) 
    grafo.adicionar_aresta("São Paulo", "Florianópolis", 696)  
    grafo.adicionar_aresta("São Paulo", "Rio de Janeiro", 446)  
    grafo.adicionar_aresta("São Paulo", "Salvador", 1922) 



    grafo.adicionar_aresta("Curitiba", "Natal", 3361)  
    grafo.adicionar_aresta("Curitiba", "Belo Horizonte", 991) 
    grafo.adicionar_aresta("Curitiba", "Florianópolis", 306) 
    grafo.adicionar_aresta("Curitiba", "Rio de Janeiro", 853)  
    grafo.adicionar_aresta("Curitiba", "Salvador", 2399) 


    caminhoes = [Caminhao(capacidade=5000, limite_horas=15), Caminhao(capacidade=7000, limite_horas=10)]
    
    entregas = [
        Entrega("Natal", peso=3000, prazo_dias=2), 
        Entrega("Belo Horizonte", peso=1500, prazo_dias=1),
        Entrega("Florianópolis", peso=4000, prazo_dias=3), 
        Entrega("Rio de Janeiro", peso=2000, prazo_dias=2), 
        Entrega("Salvador", peso=2500, prazo_dias=90)        
    ]

    print("Entregas a serem realizadas:\n")
    for entrega in entregas:
        print(f"Destino: {entrega.destino}, Peso: {entrega.peso}kg, Prazo: {entrega.prazo_dias} dias")
    print("\n")

    alocar_caminhoes(grafo, caminhoes, entregas)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    print(f"\n Tempo de execução da função: {tempo_execucao:.4f} segundos \n")
    analisar_uso_memoria(grafo, caminhoes, entregas)


if __name__ == "__main__":

    executar_poucas_entregas_rotas_curtas()
    executar_muitas_entregas_rotas_longas()