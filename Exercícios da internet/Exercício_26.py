"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    1.Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    2.Triângulo Equilátero: três lados iguais;
    3.Triângulo Isósceles: quaisquer dois lados iguais;
    4.Triângulo Escaleno: três lados diferentes;
"""
class treino:
    def __init__(self):
        self.triangulo = []
        for indice in range(3):
            while True:
                print(" ")
                lado = input(f"Digite a lado {indice +1}:")
                if self.verificarNumero(lado):
                    self.colocarLados(lado)
                    break
                else:
                    continue
        self.calcular()

    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def colocarLados(self, lado):
        self.triangulo.append(float(lado))

    def calcular(self):
        self.verificarTriangulo()
        self.tipoTriangulo()
    
    def verificarTriangulo(self):
        if self.triangulo[0] + self.triangulo[1] > self.triangulo[2]:
            self.conceito = True
        elif self.triangulo[0] + self.triangulo[2] > self.triangulo[1]:
            self.conceito = True
        elif self.triangulo[2] + self.triangulo[1] > self.triangulo[0]:
            self.conceito = True
        else:
            self.conceito = False
    def tipoTriangulo(self):
        if self.conceito == True:
            if self.triangulo[0] == self.triangulo[1] == self.triangulo[2]:
                self.tipo = "Triângulo Equilátero"
                print(f"\nResultado: {self.tipo}\n")
            elif (self.triangulo[0] == self.triangulo[1]) or (self.triangulo[2] == self.triangulo[1]) or (self.triangulo[0] == self.triangulo[2]):
                self.tipo = "Triângulo Isósceles"
                print(f"\nResultado: {self.tipo}\n")
            else:
                self.tipo = "Triângulo Escaleno"
                print(f"\nResultado: {self.tipo}\n")
        else:
            print(f"\nResultado: os dados informados não geram um triângulo.\n")

resultado = treino()