"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
"""
class treino:
    def __init__(self):
        self.notas = []
        for indice in range(2):
            while True:
                print(" ")
                nota = input(f"Digite a nota {indice +1}:")
                if self.verificarNumero(nota):
                    self.colocarNotas(nota)
                    break
                else:
                    continue
        self.calcularMedia()

    def verificarNumero(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def colocarNotas(self, nota):
        self.notas.append(float(nota))

    def calcularMedia(self):
        soma = sum(self.notas)
        media = soma / len(self.notas)
        self.situacaoMediaAproveitamento(media)
        self.situacaoAluno()
        print(f"\nA média do Aluno foi : {media}, ou seja, o aluno  foi {self.situacao} com conceito ({self.conceito})\n")
    
    def situacaoMediaAproveitamento(self,media):
        if media <= 10  and media > 9:
            self.conceito = "A"
        elif media <= 9 and media > 7.5:
            self.conceito = "B"
        elif media <= 7.5 and media > 6:
            self.conceito = "C"
        elif media <= 6 and media > 4:
            self.conceito = "D"
        elif media <= 4 and media > 0:
            self.conceito = "E"
        else:
            self.conceito = "F"
    def situacaoAluno(self):
        if self.conceito == "A":
            self.situacao = "Aprovado com Distinção"
        elif self.conceito == "B" or self.conceito == "C":
            self.situacao = "Aprovado"
        elif self.conceito == "D" or self.conceito == "E" or self.conceito == "F":
            self.situacao = "Reprovado"

resultado = treino()