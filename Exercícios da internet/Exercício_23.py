"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  1.Salário Bruto até 900 (inclusive) - isento
  2.Salário Bruto até 1500 (inclusive) - desconto de 5%
  3.Salário Bruto até 2500 (inclusive) - desconto de 10%
  4.Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

class treino:
    def __init__(self):
        self.FGTS = 0.11
        self.INSS = 0.1
        self.SIND = 0.03
        while True:
          ganhaPorHora = input("Digite o quanto você ganha por hora: ")
          if self.verificarNumero(ganhaPorHora):
              self.ganhaPorHora = float(ganhaPorHora)
              break
        while True:
          horasTrabalhadas = input("Digite o número de horas trabalhadas no mês: ")
          if self.verificarNumero(horasTrabalhadas):
            self.horasTrabalhadas = float(horasTrabalhadas)
            break
        self.analiseIR() 
        self.calculo()       
        self.final()

    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def analiseIR(self):
        self.salarioBruto = self.ganhaPorHora * self.horasTrabalhadas    
        if self.salarioBruto <= 900:
            self.descontoIR = 1
            self.logotimoIR = "Isento"
        elif self.salarioBruto >900 and self.salarioBruto <= 1500:
            self.descontoIR = 0.05
            self.logotimoIR = "5%"
        elif self.salarioBruto > 1500 and self.salarioBruto <= 2500:  
            self.descontoIR = 0.1
            self.logotimoIR = "10%"
        else:
            self.descontoIR = 0.2
            self.logotimoIR = "20%"

    def calculo(self):    
      self.proFGTS = self.salarioBruto * self.FGTS
      self.proINSS = self.salarioBruto * self.INSS
      self.proSIND = self.salarioBruto * self.SIND
      if self.descontoIR == 1:
        self.proIR = 0
      else:
        self.proIR = self.salarioBruto * self.descontoIR
      self.salarioLiquido = self.salarioBruto - self.proINSS - self.proSIND - self.proIR
      self.totalDescontos = self.proINSS + self.proSIND + self.proIR
      
    def final(self):
      print(f"""
( * )Salário Bruto : R${self.salarioBruto:.2f}
( - )INSS (10%) : R${self.proINSS:.2f}
( - )Sindicato (3%) : R${self.proSIND:.2f}
( - )Imposto de Renda ({self.logotimoIR}) : R${self.proIR:.2f}
( * )FGTS (11%) : R${self.proFGTS:.2f}            
--------------------------------------------------------------
Total de Descontos : R${self.totalDescontos:.2f}
-------------------------------------------------------------                            
Salário Líquido : R${self.salarioLiquido:.2f}
""")

resultado = treino()