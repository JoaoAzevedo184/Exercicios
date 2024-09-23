"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    1.Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    2.Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    3.Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    4.Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
class treino:
    def __init__(self):
        print('''
    Vamos resolver a equação do segundo grau:
        a(x**2) + bx + c        
        ''')
        while True:
            a = input(f"\nDigite o valor de a:")
            if self.verificarNumero(a):
                if self.verificarA(a):
                    self.a = int(a)
                    self.demais()
                    break
                else:
                    print("A equação não é mais do segundo grau.\nFim do programa.")
                    break
            else:
                continue
    
    def demais(self):
        while True:
            b = input(f"\nDigite o valor de b:")
            if self.verificarNumero(b):
                self.b = int(b)
                break
            else:
                continue
        while True:
            c = input(f"\nDigite o valor de c:")
            if self.verificarNumero(c):
                self.c = int(c)
                break
            else:
                continue
        self.delta()

    def verificarA(self,x):
        x = int(x)
        if x == 0:
            return False
        else:
            return True
    
    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def delta(self):
        delta = (self.b**2) - (4 * self.c * self.a)
        if delta < 0:
            print("\nA equação não possui raízes reais.\nFim do programa.")
        elif delta == 0:
            print("\nA equação possui uma raiz real.")
            self.delta = delta
            self.resultado()
        else:
            print("\nA equação possui duas raízes reais.")
            self.delta = delta
            self.resultado()

    def resultado(self):
        if self.delta == 0:
            x = -self.b / (2 * self.a)
            print(f"\nA raíz da equação é {x}")
        else:
            x1 = (-self.b + self.delta) / (2 * self.a)
            x2 = (-self.b - self.delta) / (2 * self.a)
            print(f"\nAs raízes da equação são {x1:.2f} e {x2:.2f}")
resultado = treino()