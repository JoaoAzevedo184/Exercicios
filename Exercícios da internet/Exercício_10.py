"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

1. Salário bruto.
2. Quanto pagou ao INSS.
3. Quanto pagou ao sindicato.
4. O salário líquido.
5. Calcule os descontos e o salário líquido, conforme a tabela abaixo:

Salário Bruto - IR (11%) - INSS (8%) - Sindicato (5%) = Salário Liquido
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

class treino:
    def __init__(self):
        self.IR = 0.11
        self.INSS = 0.08
        self.SIND = 0.05
        while True:
            g_h = input("Digite o quanto você ganha por hora: ")
            if self.verificar(g_h):
                self.g_h = float(g_h)
                h_m = input("Digite o número de horas trabalhadas no mês: ")
                if self.verificar(h_m):
                   self.h_m = float(h_m)
                   break
        self.calculo()

    def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

    def calculo(self):
        self.s_bruto = self.g_h * self.h_m
        self.ir = self.s_bruto * self.IR
        self.inss = self.s_bruto * self.INSS
        self.s_ind = self.s_bruto * self.SIND
        self.s_liquido = self.s_bruto - self.ir - self.inss - self.s_ind
        print( f'''
        Bruto: {self.s_bruto}
        IR: {self.ir}
        INSS: {self.inss}
        Sindicato: {self.s_ind}
        Liquido: {self.s_liquido}
        ''')

resultado = treino()