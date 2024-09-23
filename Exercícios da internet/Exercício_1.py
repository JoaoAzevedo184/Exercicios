#Programa que peça dois números e imprima a soma.

class treino:
  def __init__(self):
    while True:
          n1 = input("Digite um número:")
          if self.verificar(n1):
             self.n1 = int(n1)
             break

    while True:
       n2 = input("Digite outro número:")
       if self.verificar(n2):
                self.n2 = int(n2)
                break

    self.s = self.n1+ self.n2

  def verificar(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("Por favor, digite apenas números inteiros.")
            return False

  def __str__(self):
        return f"Resultado: {self.s}"

resultado = treino()
print(resultado)