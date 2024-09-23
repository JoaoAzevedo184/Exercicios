#Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

class treino:
  def __init__(self):
      while True:
            n = input("Quanto você ganha por hora trabalhada?R$")
            if self.verificar(n):
              self.n = float(n)
              n1 = input("Qual o número de horas trabalhadas no mês:")
              if self.verificar(n1):
                 self.n1 = float(n1)
                 break

      self.calculo(self.n, self.n1)

  def calculo(self, x, y):
      self.salario= x * y

  def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

  def __str__(self):
        return f'''
        Sua folha de pagamento é de  R${self.salario}, após ter trabalhado {self.n1} horas no mês e recebendo R${self.n} por hora trabalhada.
        '''

resultado = treino()
print(resultado)