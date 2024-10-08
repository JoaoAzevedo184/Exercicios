"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	
576

Exemplo de Saída
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""
# Leitura do valor inteiro
valor = int(input("Insira valor: "))

# Armazena o valor inicial para impressão
valor_inicial = valor

# Notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Dicionário para armazenar a quantidade de cada nota
quantidade_notas = {}

# Cálculo da quantidade de cada nota
for nota in notas:
    quantidade_notas[nota] = valor // nota
    valor %= nota

# Impressão do valor lido
print(valor_inicial)

# Impressão da quantidade de cada tipo de nota
for nota in notas:
    print(f"{quantidade_notas[nota]} nota(s) de R$ {nota},00")