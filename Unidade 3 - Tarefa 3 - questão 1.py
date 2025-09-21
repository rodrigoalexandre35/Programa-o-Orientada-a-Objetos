import random
from datetime import datetime


class Usuario:
    def __init__(self, rg=0, cpf=0, nome="Padrão", dataNascimento=datetime(1900, 1, 1)):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.dataNascimento = dataNascimento


class Conta:
    def __init__(self, agencia, usuario: Usuario, dataAbertura=datetime.now(), saldo=0.0):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo


if __name__ == "__main__":
   
    usuario = Usuario()

   
    usuario.rg = int(input("Digite o RG: "))
    usuario.cpf = int(input("Digite o CPF: "))
    usuario.nome = input("Digite o nome: ")
    data_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
    usuario.dataNascimento = datetime.strptime(data_str, "%d/%m/%Y")

    agencia = random.randint(0, 999)  
    saldo = float(input("Digite o saldo inicial da conta: "))
    conta = Conta(agencia, usuario, datetime.now(), saldo)

   
    print("\n=== Dados da Conta ===")
    print(f"Agência: {conta.agencia}")
    print(f"Data de Abertura: {conta.dataAbertura.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Saldo: R$ {conta.saldo:.2f}")

    print("\n=== Dados do Usuário ===")
    print(f"Nome: {conta.usuario.nome}")
    print(f"RG: {conta.usuario.rg}")
    print(f"CPF: {conta.usuario.cpf}")
    print(f"Data de Nascimento: {conta.usuario.dataNascimento.strftime('%d/%m/%Y')}")
