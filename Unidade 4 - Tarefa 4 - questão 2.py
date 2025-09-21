class Restaurante:
    def __init__(self, nome, tipo_cozinha):
        self.nome = nome
        self.tipo_cozinha = tipo_cozinha
        self.numeroServidos = 0  

    
    def getNumeroServidos(self):
        return self.numeroServidos

   
    def setNumeroServidos(self, numero):
        self.numeroServidos = numero

    
    def incrementeNumeroServidos(self, quantidade):
        self.numeroServidos += quantidade



restaurante = Restaurante("Sabor Nordestino", "Comida Regional")

print("Clientes atendidos:", restaurante.getNumeroServidos())


restaurante.setNumeroServidos(20)
print("Depois de mudar:", restaurante.getNumeroServidos())


restaurante.incrementeNumeroServidos(5)
print("Depois de somar:", restaurante.getNumeroServidos())
