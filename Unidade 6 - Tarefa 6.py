```python
class Veiculo:
    
    total_veiculos = 0

       def __init__(self, placa: str, modelo: str, diaria: float):
        self.__placa = placa          
        self.modelo = modelo          
        self.diaria = diaria          
        self.__alugado = False        
        Veiculo.total_veiculos += 1   
    
    @property
    def placa(self):
        return self.__placa

    
    @placa.setter
    def placa(self, valor):
        print("Erro: A placa não pode ser modificada após o cadastro!")

        def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.modelo} ({self.__placa}) foi alugado.")
        else:
            print(f"Veículo {self.modelo} ({self.__placa}) já está alugado!")

       def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.modelo} ({self.__placa}) foi devolvido.")
        else:
            print(f"Veículo {self.modelo} ({self.__placa}) já está disponível!")

    def status(self):
        estado = "Alugado" if self.__alugado else "Disponível"
        print(f"Veículo {self.modelo} ({self.__placa}) está {estado}.")

 
    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos cadastrados: {cls.total_veiculos}")

    
    @staticmethod
    def calcular_preco_aluguel(dias: int, diaria: float):
        return dias * diaria



if __name__ == "__main__":
    v1 = Veiculo("ABC-1234", "Fiat Uno", 100.0)
    v2 = Veiculo("XYZ-9876", "Toyota Corolla", 200.0)

    v1.status()
    v1.alugar()
    v1.status()
    v1.devolver()
    v1.status()

    print("\nTentando alterar a placa:")
    v1.placa = "NOV-9999"  

    Veiculo.mostrar_total_veiculos()

    dias = 5
    preco = Veiculo.calcular_preco_aluguel(dias, v2.diaria)
    print(f"\nPreço para alugar {v2.modelo} por {dias} dias: R$ {preco:.2f}")
```
