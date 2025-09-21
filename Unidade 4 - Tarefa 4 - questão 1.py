class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = float(saldo)

    def consultarSaldo(self):
        print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque: R$ {valor:.2f}")
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def transferir(self, valor, outraConta):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            outraConta.saldo += valor
            print(f"Transferência de R$ {valor:.2f} para {outraConta.titular}")
            return True
        else:
            print("Saldo insuficiente para t
