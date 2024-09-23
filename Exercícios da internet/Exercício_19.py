"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

class treino:
    def __init__(self):
        self.produtos = []
        for indice in range(3):
            while True:
                print(" ")
                numero = input(f"Digite preço do produto {indice +1}:")
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
        self.produtos.append(float(numero))

    def calcularLista(self):
        menor = min(self.produtos)
        self.situacao(menor)
    
    def situacao(self, menor):
        posicao = self.produtos.index(menor)
        posicao +=1
        print(f"O produto {posicao} é o mais barato dos três produtos, pois custa R${menor:.2f}.")

resultado = treino()