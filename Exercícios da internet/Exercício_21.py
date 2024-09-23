"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

class treino:
    def __init__(self):
        print('''Digite o turno você estuda:
                [ M ] Matutino
                [ V ] Vespertino
                [ N ] Noturno
                ''')
        while True:
            turno = input("Responda: ")
            if self.verificarNumero(turno):
                turno = turno.lower()
                if self.verificarLetra(turno):
                    self.turno = turno
                    break
                else:
                    continue
            else:
                continue
        self.analise()

    def verificarNumero(self,x):
        try:
            float(x)
            print("\nValor Inválido! Por favor, digite novamente.")
            return False
        except ValueError:
            return True

    def verificarLetra(self,x):
        if x == "m":
           return True
        elif x == "v":
            return True
        elif x == "n":
            return True
        else:
            print("\nValor Inválido! Por favor, digite apenas uma letra das opções.")
            return False
    
    def analise(self):
        if self.turno == "m":
            print("\nBom Dia!")
        elif self.turno == "v":
            print("\nBoa Tarde!")
        elif self.turno == "n":
            print("\nBoa Noite!")

resultado = treino()