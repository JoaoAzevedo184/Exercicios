#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

class treino:
  def __init__(self):

    print('''Digite qual é o seu sexo:
                  [ 0 ] Masculino
                  [ 1 ] Feminino
                ''')
    while True:
          genero = input("Digite o número: ")
          if self.verificarint(genero):
              self.genero = int (genero)
              if self.genero not in range(2):
                  print("Escolha inválida. Por favor, escolha um número de 0 ou 1.")
                  continue
              break
    while True:
            altura = input("Digite a sua altura:")
            if self.verificar(altura):
              self.altura = float(altura)
              break

    self.calculo(self.altura, self.genero)

  def calculo(self, x, y):
    if y == 1:
      self.pesoideal= (62.1 * x) - 44.7
    else:
      self.pesoideal= (72.7 * x) - 58

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

  def __str__(self):
        genero_str = 'feminino' if self.genero == 1 else 'masculino'
        return f'O seu peso ideal é de {self.pesoideal:.2f} kg, pois tem {self.altura}m de altura e é do gênero {genero_str}.'

resultado = treino()
print(resultado)