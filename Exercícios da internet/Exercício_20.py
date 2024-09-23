"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

class treino:
    def __init__(self):
        self.lista = []
        for indice in range(3):
            while True:
                print(" ")
                numero = input(f"Digite o numero {indice +1}:")
                if self.verificarNumero(numero):
                    self.colocarLista(numero)
                    break
                else:
                    continue
        self.calcularLista()
        
    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def colocarLista(self, numero):
        self.lista.append(float(numero))

    def calcularLista(self):
        # Ordem decrescente
        ordemDecrescente = sorted(self.lista, reverse=True)
        print("\nOrdem decrescente:", ordemDecrescente)
        for indice, valor in enumerate(ordemDecrescente):
            print(f"{indice}: {valor}")

        # Ordem crescente
        ordemCrescente = sorted(self.lista)
        print("\nOrdem crescente:", ordemCrescente)
        for indice, valor in enumerate(ordemCrescente):
            print(f"{indice}: {valor}")

resultado = treino()