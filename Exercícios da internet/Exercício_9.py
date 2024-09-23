"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 

Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve
pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""
class treino:
    def __init__(self):
        max = 50
        while True:
            peso = input("Digite o peso do peixe: ")
            if self.verificar(peso):
                self.peso = float(peso)
                break
        if self.peso > max:
          self.excesso = self.peso - max
          self.multa_v = self.excesso * 4
          print(f"O peso dos peixes excede o limite permitido em {self.excesso:.2f}kg. Portanto, João deverá pagar uma multa de R$ {self.multa_v:.2f}.")
        else:
          print(f"O peso dos peixes está dentro do limite permitido. Nenhuma multa será aplicada.")

    def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False

resultado = treino()