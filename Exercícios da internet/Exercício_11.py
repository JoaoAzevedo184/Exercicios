"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
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
        print("O tamanho em metros quadrados da área a ser pintada é de {:.2f}".format(self.a_p))
        self.calculo()

    def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

    def calculo(self):
        self.litrosTinta = self.a_p / 3
        print("Litros de Tinta necessários: {:.2f}L".format(self.litrosTinta))

        self.latas = self.litrosTinta / 18
        print("Latas necessárias: {:.2f}".format(self.latas))

        self.reais = self.latas * 80 + self.litrosTinta * 18/80
        print("Total a gastar: R${:.2f}".format(self.reais))


resultado = treino()