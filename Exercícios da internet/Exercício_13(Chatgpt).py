"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
"""

from datetime import timedelta

class Treino:
    def __init__(self):
        while True:
            arquivo_download = input("Digite o tamanho do arquivo que deseja baixar (em MB): ")
            if self.verificar(arquivo_download):
                self.arquivo_download = float(arquivo_download)
                break
        while True:
            velocidade_internet = input("Digite a velocidade de sua internet (em Mbps): ")
            if self.verificar(velocidade_internet):
                self.velocidade_internet = float(velocidade_internet)
                break
        self.calculo()

    def verificar(self, x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite um número válido.")
            return False
    
    def calculo(self):
        arquivo_download_mbps = self.arquivo_download * 8
        segundos = arquivo_download_mbps / self.velocidade_internet
        tempo = timedelta(seconds=segundos)
        
        horas = tempo.seconds // 3600
        minutos = (tempo.seconds // 60) % 60
        segundos = tempo.seconds % 60

        if horas > 0:
            print(f"O tempo aproximado de download do arquivo é de {horas} horas, {minutos} minutos e {segundos} segundos.")
        else:
            print(f"O tempo aproximado de download do arquivo é de {minutos} minutos e {segundos} segundos.")

resultado = Treino()