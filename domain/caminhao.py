class Caminhao:
    def __init__(self, capacidade, limite_horas):
        self.capacidade = capacidade        
        self.limite_horas = limite_horas   
        self.carga_atual = 0
        self.entregas = []       

    def pode_alocar(self, peso_entrega):
        return self.carga_atual + peso_entrega <= self.capacidade

    def alocar_entrega(self, peso_entrega):
        self.carga_atual += peso_entrega
        self.entregas.append(peso_entrega)

    def horas_disponiveis(self):
        return self.limite_horas
