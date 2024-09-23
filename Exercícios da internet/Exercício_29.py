"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
class treino:
    def __init__(self):
        while True:
            if not self.Dia():
                break
        while True:
            if not self.Mes():
                break
        while True:            
            if not self.Ano():
                break
        while True:
            if self.verificarMes(self.mes):
                break
            else:
                if not self.Mes():
                    continue
                else: 
                    continue
        self.data()
    def Dia(self):
        while True:
            dia = input(f"\nDigite o dia:")
            if self.verificar(dia):
                self.dia = int(dia)
                break
    def Mes(self):
        while True:
            mes = input(f"\nDigite o mês:")
            if self.verificar(mes):
                self.mes = int(mes)
                break
    def Ano(self):
        while True:
            ano = input(f"\nDigite o ano:")
            if self.verificarAno(ano):
                self.ano = int(ano)
                break
            else:
                continue

    def verificar(self,x):
        try:
            if int(x)>0:
                return True
            else:
                print("\nPor favor, digite apenas números positivos e maiores que zero.")
                return False
        except ValueError:
            print("\nPor favor, digite apenas números inteiros")
            return False

    def verificarAno(self, x):
        try:
            if int(x)>=0:
                return True
            else:
                print("\nPor favor, digite apenas números positivos")
                return False
        except ValueError:
            print("\nPor favor, digite apenas números inteiros")
            return False 

    def verificarMes(self,x):
        try:
            if int(x)>0:
                if x > 12:
                    return False
                if x in [1, 3, 5, 7, 8, 10, 12]:
                    if self.dia > 31:
                        return False
                elif x in [4, 6, 9, 11]:
                    if self.dia > 30:
                        return False
                elif x == 2:
                    if (self.ano % 4 == 0 and self.ano % 100 != 0) or self.ano % 400 == 0:
                        if self.dia <= 1 or self.dia > 29:
                            return False
                    else:
                        if self.dia <= 1 or self.dia > 28:
                            return False
                else:
                    return False
                return True
            else:
                print("\nPor favor, digite apenas números positivos e maiores que zero.")
                return False
        except ValueError:
            print("\nPor favor, digite apenas números inteiros")
            return False       
    def data(self):
        if self.mes < 10:
            if self.dia < 10:
                print(f"0{self.dia}/0{self.mes}/{self.ano}")
            else:
                print(f"{self.dia}/0{self.mes}/{self.ano}")
        else:
            if self.dia < 10:
                print(f"0{self.dia}/{self.mes}/{self.ano}")
            else:
                print(f"{self.dia}/{self.mes}/{self.ano}")

resultado = treino()