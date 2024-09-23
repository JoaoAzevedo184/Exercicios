"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

class treino:
    def __init__(self):
        self.vogais = ["a","e","i","o","u"]
        while True:
            letra = input("\nDigite uma letra qualquer:")
            if self.verificarNumero(letra):
                if self.verificarLetra(letra):
                    letra = letra.lower()
                    self.analise(letra)
                    break
                else:
                    continue
            else:
                continue

    def verificarNumero(self,x):
        try:
            float(x)
            print("\nPor favor, digite alguma letra.")
            return False
        except ValueError:
            return True

    def verificarLetra(self, letra):
        if len(letra) > 1:
            print("\nDigite apenas uma letra.")
            return False
        else:
            return True

    def analise(self, letra):
        if letra in self.vogais:
            print("\nA sua letra é uma vogal.")
        else:
            print("\nA sua letra é uma consoante.") 

resultado = treino()