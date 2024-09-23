"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

1.Comprar apenas latas de 18 litros;
2.Comprar apenas galões de 3,6 litros;
3.Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
4.Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

"""
math.ceil() é uma função em Python que retorna o menor número inteiro maior ou igual ao número passado como argumento. Em outras palavras, ele arredonda um número para cima.
math.floor()é uma função em Python que retorna o menor número inteiro menor ou igual ao número passado como argumento. Em outras palavras, ele arredonda um número para baixo.
"""

class treino:
    def __init__(self):
        while True:
          largura = input("Digite a largura da parede em metros: ")
          if self.verificar(largura):
              self.largura = float(largura)
              break
        while True:      
          altura = input("Digite a altura da parede em metros: ")
          if self.verificar(altura):
              self.altura = float(altura)
              break

        self.a_p = self.largura * self.altura
        print("\nO tamanho em metros quadrados da área a ser pintada é de {:.2f}".format(self.a_p))
        self.calculoLitros()
        self.calculoLatas()
        self.calculoGalao()
        self.calcularMistura()

    def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

    def calculoLitros(self):
        self.litrosTintas = self.a_p / 6 * 0.1
        print("\nLitros necessários: {:.2f}L".format(self.litrosTintas))

    def calculoLatas(self):
        self.latas = math.ceil(self.litrosTintas / 18)
        print(f"\nLatas necessárias: {self.latas}")

        self.reaisLatas = self.latas * 80
        print(f"Total a gastar com Latas: R${self.reaisLatas}")

    def calculoGalao(self):
        self.galao = math.ceil(self.litrosTintas / 3.6)
        print(f"\nGalões necessárias: {self.galao}")

        self.reaisGalao = self.galao * 25
        print(f"Total a gastar com Galões: R${self.reaisGalao}")

    def calcularMistura(self):
        self.latasCheias = int(self.litrosTintas // 18)
        self.galoesCheios = math.ceil((self.litrosTintas % 18) / 3.6)
        self.reaisGalao = self.galoesCheios * 25
        self.reaisLatas = self.latasCheias * 80
        
        print(f'''\nTotal a gastar juntando:
    Latas: R${self.reaisLatas}
    Galões: R${self.reaisGalao}''')

resultado = treino()