import math
"""
OBI2010
Caderno de Tarefas
Modalidade Programaçao • Nível 1, Fase 2
8 de maio de 2010

Sedex Marciano
"""


#função para verificar se é um número
def Verificar(x):
    try:
        if x.isdigit():
            return True
        elif x.alpha():
            return False
    except ValueError:    
        return False
        
def VolumeCubo(x, y,z):
    return x*y*z

def VoleumeEsfera(x):
    return (pow(x,3)*4*math.pi)/3

#função para saber se é possível ou não
def Comparacao(x,y):
    if x <= y:
        return 'S'
    else:
        return 'N'
    
#função para saber o máximo ou mínimo de um inteiro    
def MinMax(x):
    if 0 <= x <=1000:
        return True
    else:
        return False
#tupla para analisar as variaveis
variaveis =[]

while True:
    L,A,P,R= map(str, input().split()) 
    if Verificar(L) and Verificar(A) and Verificar(P) and Verificar(R):
        L=int(L)
        A=int(A)
        P=int(P)
        R=int(R)
        variaveis.append(L)
        variaveis.append(A)
        variaveis.append(P)
        variaveis.append(R)
        
        #analisar as quatros variaveis de uma vez
        if all(MinMax(v) for v in variaveis):
          break
        else:
            print("Digite apenas números entre 0 e 1000.")
            continue
    else:
        print("Digite apenas números e não esqueça de apertar a tecla espaço.")
        continue

Vcubo = VolumeCubo(L,A,P)
Vesfera = VoleumeEsfera(R)
Resultado = Comparacao(Vcubo,Vesfera)
print(Resultado)