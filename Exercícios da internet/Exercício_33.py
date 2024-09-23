"""
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

Entrada
O arquivo de entrada contém um valor inteiro.

Saída
Imprima a saída conforme exemplo fornecido.

Exemplo de Entrada	
400

Exemplo de Saída
1 ano(s)
1 mes(es)
5 dia(s)
"""
# Leitura do valor inteiro que representa a idade em dias
valor = int(input("Insira valor: "))

# Definição das unidades de tempo em dias
tempos = [365, 30, 1]

# Inicialização do dicionário com as chaves corretas
quantidade_tempos = {
    "ano(s)": 0,
    "mes(es)": 0,
    "dia(s)": 0
}

# Lista de chaves correspondente às unidades de tempo
chaves = ["ano(s)", "mes(es)", "dia(s)"]

# Cálculo da quantidade de anos, meses e dias
for i, tempo in enumerate(tempos):
    quantidade_tempos[chaves[i]] = valor // tempo
    valor %= tempo

# Impressão do resultado
for chave, quantidade in quantidade_tempos.items():
    print(f"{quantidade} {chave}")