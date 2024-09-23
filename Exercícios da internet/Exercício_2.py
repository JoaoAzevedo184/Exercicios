#Programa que peça as 4 notas bimestrais e mostre a média.

class treino:
  def __init__(self):
    while True:
          n1 = input("Digite primeira nota:")
          if self.verificar(n1):
             self.n1 = float(n1)
             break

    while True:
       n2 = input("Digite segunda nota:")
       if self.verificar(n2):
                self.n2 = float(n2)
                break
    while True:
       n3 = input("Digite terceira nota:")
       if self.verificar(n3):
                self.n3 = float(n3)
                break
    while True:
       n4 = input("Digite quarta nota:")
       if self.verificar(n4):
                self.n4 = float(n4)
                break

    self.s = self.n1+ self.n2 + self.n3 + self.n4
    self.m = self.s/4

  def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

  def __str__(self):
        return f"Média: {self.m}"

resultado = treino()
print(resultado)