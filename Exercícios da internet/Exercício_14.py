"""
1.Faça um Programa que peça dois números e imprima o maior deles.
2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

class treino:
    def __init__(self):
        while True:
            number1 = input("Digite o número 1: ")
            if self.verificar(number1):
                self.number1 = int(number1)
                break
        while True:
            number2 = input("Digite o number 2: ")
            if self.verificar(number2):
                self.number2 = int(number2)
                break
        self.comparacao()
        self.valor()

    def verificar(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False
    
    def comparacao(self):
        if self.number1 > self.number2:
            print(f"{self.number1} é maior que {self.number2}")
        elif self.number1 == self.number2:
            print(f"{self.number1} é igual que {self.number2}")
        else:
            print(f"{self.number2} é maior que {self.number1}")

    def valor(self):
        if self.number1 > 0 :
            print(f"{self.number1} é positivo")
        elif self.number1 == 0:
            print(f"{self.number1} é neutro, pois é zero")
        else:
            print(f"{self.number1} é negativo")

        if self.number2 > 0 :
            print(f"{self.number2} é positivo")
        elif self.number2 == 0:
            print(f"{self.number2} é neutro, pois é zero")
        else:
            print(f"{self.number2} é negativo")
        
resultado = treino()