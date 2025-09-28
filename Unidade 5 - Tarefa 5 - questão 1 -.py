```python

class CartaoWeb:
    def __init__(self, destinatario):
        self.destinatario = destinatario

    def showMessage(self):
        print("Mensagem genérica do cartão.")

class DiaDosNamorados(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}! ❤️")


class Natal(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}! 🎄🎅")


class Aniversario(CartaoWeb):
    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}! 🎉🥳")


if __name__ == "__main__":
    cartao = DiaDosNamorados("Maria")
    cartao.showMessage()

    cartao = Natal("João")
    cartao.showMessage()

    cartao = Aniversario("Ana")
    cartao.showMessage()


# Explicação (Polimorfismo):
# A variável "cartao" é sempre do tipo CartaoWeb,
# mas pode guardar objetos diferentes (DiaDosNamorados, Natal ou Aniversario).
# Quando chamamos showMessage(), o Python executa o método da classe correta.
# Isso é polimorfismo: o mesmo nome de método com comportamentos diferentes.
```
