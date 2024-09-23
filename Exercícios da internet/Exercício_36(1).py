# Lê o número de intervalos
n = int(input())

# Inicializa a distância total
distancia_total = 0

# Para cada intervalo, calcula a distância e adiciona à distância total
for _ in range(n):
    t, v = map(int, input().split())
    distancia_total += t * v

# Imprime a distância total
print(distancia_total)