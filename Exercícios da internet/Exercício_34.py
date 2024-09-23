"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	
576.73

Exemplo de Saída
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
"""

# Leitura do valor inteiro
valor = float(input("Insira valor: "))

# Notas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1 , 0.50, 0.25, 0.10, 0.05, 0.01]

# Dicionário para armazenar a quantidade de cada nota
quantidade_notas = {}
quantidade_moedas = {}

# Cálculo da quantidade de cada nota
for nota in notas:
    quantidade_notas[nota] = int(valor // nota)
    valor %= nota

for moeda in moedas:
    quantidade_moedas[moeda] = int(valor // moeda)
    valor %= moeda

# Impressão da quantidade de cada tipo de nota
print("NOTAS:")
for nota in notas:
    print(f"{quantidade_notas[nota]} nota(s) de R$ {nota}.00")
print("MOEDAS:")
for moeda in moedas:
    print(f"{quantidade_moedas[moeda]} moeda(s) de R$ {moeda:.2f}")