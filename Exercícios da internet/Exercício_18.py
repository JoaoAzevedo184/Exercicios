"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

class treino:
    def __init__(self):
        self.lista = []
        for indice in range(3):
            while True:
                print(" ")
                numero = input(f"Digite o numero {indice +1}:")
                if self.verificarNumero(numero):
                    self.colocarLista(numero)
                    break
                else:
                    continue
        self.calcularLista()
        
    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def colocarLista(self, numero):
        self.lista.append(float(numero))

    def calcularLista(self):
        maior = max(self.lista)
        menor = min(self.lista)
        self.situacao(maior, menor)
    
    def situacao(self,maior, menor):
        print(f"{maior} é o maior dos três números.")
        print(f"{menor} é o menor dos três números.")

resultado = treino()