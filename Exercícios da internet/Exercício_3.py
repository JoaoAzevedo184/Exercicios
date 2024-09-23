#Programa que converta metros para centímetros.

class treino:
  def __init__(self):
      self.opções = ("km", "hm", "dam", "m", "dm", "cm", "mm")

      print('''Digite a unidade de medida base para a conversão:
                  [ 0 ] Quilômetro (km)
                  [ 1 ] Hectômetro (hm)
                  [ 2 ] Decâmetro (dam)
                  [ 3 ] Metro (m)
                  [ 4 ] Decímetro (dm)
                  [ 5 ] Centímetro (cm)
                  [ 6 ] Milímetro (mm)

                ''')
      while True:
          medida = input("Digite o número: ")
          if self.verificarint(medida):
              self.medida = int(medida)
              if self.medida not in range(7):
                  print("Escolha inválida. Por favor, escolha um número de 0 a 6.")
                  continue
              break
      print('''Digite a unidade de medida que deseja chegar:
                  [ 0 ] Quilômetro (km)
                  [ 1 ] Hectômetro (hm)
                  [ 2 ] Decâmetro (dam)
                  [ 3 ] Metro (m)
                  [ 4 ] Decímetro (dm)
                  [ 5 ] Centímetro (cm)
                  [ 6 ] Milímetro (mm)

                ''')
      while True:
          medida1 = input("Digite o número: ")
          if self.verificarint(medida1):
              self.medida1 = int(medida1)
              if self.medida1 not in range(7):
                  print("Escolha inválida. Por favor, escolha um número de 0 a 6.")
                  continue
              break
      while True:
            n1 = input("Digite a quantidade que deseja converter:")
            if self.verificar(n1):
              self.n1 = float(n1)
              break

      self.calculo(self.medida, self.medida1, self.n1)

  def calculo(self, x, y, z):
        if x == y:
            self.m = z
        else:
            conversion_factors = [1, 10, 100, 1000, 10000, 100000, 1000000]
            self.m = z * conversion_factors[y] / conversion_factors[x]

  def __str__(self):
         return f"Resultado: {self.m} {self.opções[self.medida1]}"

  def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False
  def verificarint(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

resultado = treino()
print(resultado)