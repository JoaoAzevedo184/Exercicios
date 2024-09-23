#Programa que peça 2 números inteiros e um número real.

#Calcule e mostre:

#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

class treino:
  def __init__(self):
      while True:
            n1 = input("Digite o primeiro número inteiro:")
            if self.verificarint(n1):
              self.n1 = int(n1)
              break

      while True:
            n2 = input("Digite o segundo número inteiro:")
            if self.verificarint(n2):
              self.n2 = int(n2)
              break

      while True:
            r = input("Digite um número real:")
            if self.verificarreal(r):
              self.r = float(r)
              break

      self.calculo(self.n1, self.n2, self.r)

  def calculo(self, x, y, z):
      self.o1= (2 * x) * (y/2)
      self.o2= (3 * x) + y
      self.o3=  (z**3)

  def verificarint(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False
  def verificarreal(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

  def __str__(self):
        return f'''
  a) o produto do dobro do primeiro com metade do segundo. R={self.o1}

  b) a soma do triplo do primeiro com o terceiro. R={self.o2}

  c) o terceiro elevado ao cubo. R={self.o3}
        '''

resultado = treino()
print(resultado)