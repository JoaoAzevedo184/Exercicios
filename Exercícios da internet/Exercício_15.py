"""
1.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

class treino:
    def __init__(self):
        print('''Digite qual é o seu sexo:
                [ M ] Masculino
                [ F ] Feminino
                [ I ] Desejo não informar
                ''')
        while True:
            genero = input("Digite o seu gênero: ")
            if self.verificarNumero(genero):
                genero = genero.lower()
                if self.verificarLetra(genero):
                    self.genero = genero
                    break
                else:
                    continue
            else:
                continue
        self.analise()

    def verificarNumero(self,x):
        try:
            float(x)
            print("\nPor favor, digite novamente.")
            return False
        except ValueError:
            return True

    def verificarLetra(self,x):
        if x == "m":
           return True
        elif x == "f":
            return True
        elif x == "i":
            return True
        else:
            print("\nPor favor, selecione uma das opções.")
            return False
    
    def analise(self):
        if self.genero == "m":
            print("\nTu é homem.")
        elif self.genero == "f":
            print("\nTu é mulher.")
        elif self.genero == "i":
            print("\nVai te lascar.")

resultado = treino()