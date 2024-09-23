#Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class treino:
  def __init__(self):

      while True:
            lado = input("Digite o lado do quadrado:")
            if self.verificar(lado):
              self.lado = float(lado)
              break
      self.calculo(self.lado)

  def calculo(self, x):
      self.área= (x**2)
      self.área2= 2 * self.área

  def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

  def __str__(self):
        return f'''
        Área: {self.área}
        Dobro da Área: {self.área2}
        '''

resultado = treino()
print(resultado)