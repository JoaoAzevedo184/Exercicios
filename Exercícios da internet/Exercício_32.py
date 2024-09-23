"""
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

Exemplo de Entrada	
556

Exemplo de Saída
0:9:16
"""
N = int(input())
tempos = [3600, 60 ,1]
quantidade_tempo = {}
for tempo in tempos:
    quantidade_tempo[tempo] = N // tempo
    N %=tempo
"""
for tempo, quantidade in quantidade_tempo.items(): 
    print(f"{quantidade}", end=":")
"""

print(":".join(map(str, quantidade_tempo)))
"""
Usamos map para converter cada valor em quantidade_tempo para string, e join para unir esses valores com dois pontos como separador. Isso garante que não haja dois pontos no final da string.
"""