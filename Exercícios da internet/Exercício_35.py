"""
A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

Entrada
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

Saída
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.
"""
import sys
from math import gcd


def fracaoSimplificada(numerador, denominador):
    MDC = gcd(numerador, denominador)
    return numerador // MDC, denominador // MDC

def operacao(N1, D1, x, N2, D2):
    if x == '+':
        numerador = (N1*D2 + N2*D1)
        denominador = (D1*D2)
    elif x == '-':
        numerador = (N1*D2 - N2*D1)
        denominador = (D1*D2)
    elif x == '*':
        numerador = (N1*N2)
        denominador = (D1*D2)
    elif x == '/':
        numerador = (N1*D2)
        denominador = (D1*N2)
    else:
        raise ValueError("Operação inválida")
    return numerador, denominador

            
def main():
    N1,D1 = map(int, input('Digite os números: ').split("/"))
    N2,D2 = map(int, input('Digite os números: ').split("/"))
    op = input("selecione a operação( +,-,*,/):")
    results =[]
    
    numerador, denominador = operacao(N1, D1, op, N2, D2)
    numeradorSimplificado, denominadorSimplificado = fracaoSimplificada(numerador, denominador)
            
    if numeradorSimplificado == numerador and denominadorSimplificado == denominador:
        result = f"{numerador}/{denominador} = {numerador}/{denominador}"
    else:
        result = f"{numerador}/{denominador} = {numeradorSimplificado}/{denominadorSimplificado}"
            
    results.append(result)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()