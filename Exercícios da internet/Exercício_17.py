"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    1.A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    2.A mensagem "Reprovado", se a média for menor do que sete;
    3.A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

class treino:
    def __init__(self):
        self.notas = []
        for indice in range(4):
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
        self.situacaoAluno(media)
        print(f"\nA média do Aluno foi : {media}, ou seja, o aluno  foi {self.situacao}\n")
    
    def situacaoAluno(self,media):
        if media == 10:
            self.situacao = "Aprovado com Distinção"
        elif media>=7:
            self.situacao = "Aprovado"
        else:
            self.situacao = "Reprovado"

resultado = treino()