"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
class treino:
    def __init__(self):
        self.semana = ["domingo","segunda","terça","quarta","quinta","sexta","sabado"]
        print("""Digite o número correspondente ao dia da semana:
              [ 0 ] Domingo
              [ 1 ] Segunda
              [ 2 ] Terça
              [ 3 ] Quarta
              [ 4 ] Quinta
              [ 5 ] Sexta
              [ 6 ] Sábado
              """)
        while True:
            dia = input("\nResponda:")
            if self.verificarNumero(dia):
                dia = int(dia)
                if dia not in range(7):
                    print("Por favor, digite um número de 0 a 6.")
                    continue
                else:
                    break

        self.dia = int(dia)
        print(f"O dia da semana é {self.semana[self.dia]}")

    def verificarNumero(self,x):
        try:
            int(x)
            return True
        except ValueError:
            print("\nValor inválido!Por favor, digite novamente.")
            return False

resultado = treino()
