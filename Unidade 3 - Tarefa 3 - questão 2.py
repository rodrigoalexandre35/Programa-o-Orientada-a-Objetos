class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está aberto!")

    def __str__(self):  
        return f"Restaurante: {self.nomeRestaurante} | Tipo: {self.tipoCozinha}"



r1 = Restaurante("Sabor Nordestino", "Comida Típica")
r2 = Restaurante("Itália Bella", "Culinária Italiana")
r3 = Restaurante("Sushi Prime", "Japonesa")


print(r1)
print(r2)
print(r3)


r1.abrirRestaurante()
