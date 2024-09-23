"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    1.salários até R$ 280,00 (incluindo) : aumento de 20%
    2.salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    3.salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    4.salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
    1.o salário antes do reajuste;
    2.o percentual de aumento aplicado;
    3.o valor do aumento;
    4.o novo salário, após o aumento.
"""

class treino:
    def __init__(self):
        while True:
            salario = input("Digite o seu salário: ")
            if self.verificarNumero(salario):
                self.salario = float(salario)
                print(f"R${self.salario:.2f}")
                break
            else:
                continue
        self.analise()

    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False
    
    def analise(self):
        if self.salario < 280:
          percentual = 20
          aumento = self.salario * 0.20
        elif self.salario >= 280 and self.salario < 700:
          percentual = 15
          aumento = self.salario * 0.15
        elif self.salario >= 700 and self.salario < 1500:
          percentual = 10
          aumento = self.salario * 0.10
        else:
          percentual = 5
          aumento = self.salario * 0.05
        
        novoSalario = self.salario + aumento
        print(f"\nO seu salário antes do reajuste era R${self.salario:.2f}")
        print(f"\nO percentual de aumento aplicado foi de {percentual}%")
        print(f"\nO valor do aumento foi de R${aumento:.2f}")
        print(f"\nO novo salário, após o aumento, é de R${novoSalario:.2f}")

resultado = treino()