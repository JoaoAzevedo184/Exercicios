"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""
class treino:
    def __init__(self):
        while True:
            ano = input(f"\nDigite um ano e veja se é bissexto:")
            if self.verificarNumero(ano):
                ano = int(ano)
                if self.verificarAno(ano):
                    self.ano = ano
                    break
                else:
                    continue
            else:
                continue
        self.resultado()

    def verificarAno(self, ano):
        if len(str(ano)) >= 4:
            return True
        else:
            print("\nDigite quatro dígitos ou mais para continuar.")
            return False
    
    def verificarNumero(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("\nPor favor, digite apenas números inteiros")
            return False

    def resultado(self):
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            print(f"\nEste ano,{self.ano}, é um ano bissexto.")
        else:
            print(f"\nEste ano,{self.ano}, não é um ano bissexto.")


resultado = treino()