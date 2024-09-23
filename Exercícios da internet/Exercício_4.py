#Programa que peça o raio de um círculo, calcule e mostre sua área.

class treino:
  def __init__(self):
      while True:
            r = input("Digite o raio do circulo:")
            if self.verificar(r):
              self.r = float(r)
              break
      self.calculo(self.r)

  def calculo(self, x):
      pi = 3.14
      self.área= pi*(x**2)

  def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

  def __str__(self):
        return f"Área: {self.área}"

resultado = treino()
print(resultado)