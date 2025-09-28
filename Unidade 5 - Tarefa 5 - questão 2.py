```python

class MetodoPagamento:
    def __init__(self, valor: float):
        self.valor = valor
   
    def pagar(self):
        print("Método de pagamento genérico.")


class CartaoCredito(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 1.05  
        print("\nPagamento com Cartão de Crédito")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Valor final (com taxa de 5%): R$ {valor_final:.2f}")


class BoletoBancario(MetodoPagamento):
    def pagar(self):
        valor_final = self.valor * 0.98          print("\nPagamento com Boleto Bancário")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Valor final (com desconto de 2%): R$ {valor_final:.2f}")



class Pix(MetodoPagamento):
    def pagar(self):
        print("\nPagamento com Pix")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Valor final: R$ {self.valor:.2f}")



if __name__ == "__main__":
    valor = float(input("Digite o valor da compra: R$ "))

    print("\nEscolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto Bancário")
    print("3 - Pix")

    escolha = input("Opção: ")

  
    pagamento = None

    if escolha == "1":
        pagamento = CartaoCredito(valor)
    elif escolha == "2":
        pagamento = BoletoBancario(valor)
    elif escolha == "3":
        pagamento = Pix(valor)
    else:
        print("Opção inválida!")

    if pagamento:
        pagamento.pagar()


# -----------------------------
# Explicação (Polimorfismo):
# A variável "pagamento" pode guardar objetos diferentes
# (CartaoCredito, BoletoBancario ou Pix).
# Mesmo sendo a mesma variável, o método pagar() funciona
# de forma diferente conforme o tipo do objeto.
# Vantagens de usar uma classe base (mesmo simples):
# - Organiza o código, mantendo um padrão;
# - Facilita adicionar novos métodos de pagamento depois;
# - Evita duplicar código no programa principal.
# -----------------------------
```