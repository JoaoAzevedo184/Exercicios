"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)
"""

class treino:
    def __init__(self):
        while True:
            arquivoDownload = input("Digite o tamanho do arquivo que deseja baixar(em MB): ")
            if self.verificar(arquivoDownload):
                self.arquivoDownload = float(arquivoDownload)
                break
        while True:
            velocidadeInternet = input("Digite a velocidade de sua internet(em Mbps): ")
            if self.verificar(velocidadeInternet):
                self.velocidadeInternet = float(velocidadeInternet)
                break

        self.calculo()

    def verificar(self,x):
        try:
            float(x)
            return True
        except ValueError:
            print("Por favor, digite novamente.")
            return False
    
    def calculo(self):
        self.arquivoDownloadMbps= self.arquivoDownload * 8
        segundos = self.arquivoDownloadMbps/self.velocidadeInternet

        horas = int(segundos / 3600)
        minutos = int((segundos % 3600) / 60)
        segundos = int(segundos % 60)

        if horas > 0:
            print(f"O tempo aproximado de download do arquivo é de {horas} horas, {minutos} minutos e {segundos} segundos, ou seja, {horas}:{minutos}:{segundos}.")
        else:
            print(f"O  aproximado de download do arquivo é de {minutos} minutos e {segundos} segundos, ou seja, 00:{minutos}:{segundos}.")

resultado = treino()