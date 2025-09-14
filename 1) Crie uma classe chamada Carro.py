class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor


# Criando dois carros diferentes
carro1 = Carro("Toyota", "Corolla", 2020, "Prata")
carro2 = Carro("Honda", "Civic", 2022, "Preto")

# Mostrando informações
print("Carro 1:", carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
print("Carro 2:", carro2.marca, carro2.modelo, carro2.ano, carro2.cor)
