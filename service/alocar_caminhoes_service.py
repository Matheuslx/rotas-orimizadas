def alocar_caminhoes(grafo, caminhoes, entregas):
    # Considerando a velocidade média como 80 km/h
    velocidade_media = 80
    centros = ["Belém", "Recife", "São Paulo", "Curitiba"] 

    for entrega in entregas:
        # Buscando as distâncias dos centros de distribuição até o destino
        distancias = {centro: grafo.dijkstra(centro)[entrega.destino] for centro in centros}
        
        # Encontrar o centro mais próximo
        centro_mais_proximo = min(distancias, key=distancias.get)
        tempo_viagem = distancias[centro_mais_proximo] / velocidade_media
        
        for caminhao in caminhoes:
            # Tempo total inclui o tempo da viagem e o tempo de operação do caminhão
            tempo_total = tempo_viagem + (caminhao.carga_atual / caminhao.capacidade) * caminhao.limite_horas

            # Verificando se o caminhão pode alocar a entrega considerando o peso e o prazo da entrega
            if caminhao.pode_alocar(entrega.peso) and tempo_total <= entrega.prazo_dias:
                caminhao.alocar_entrega(entrega.peso)
                print(f"Entrega de {entrega.peso}kg com destino {entrega.destino} alocada ao caminhão com capacidade {caminhao.capacidade}kg, saindo de {centro_mais_proximo}.")
                break
        else:
            print(f"Não há caminhões disponíveis para a entrega de {entrega.peso}kg para {entrega.destino}.")
