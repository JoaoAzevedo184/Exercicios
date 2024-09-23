def decomporValor(n):
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
    
    print("NOTAS:")
    for nota in notas:
        num_notas = int(n // nota)
        n -= num_notas * nota
        print(f"{num_notas} nota(s) de R$ {nota:.2f}")

    print("MOEDAS:")
    for moeda in moedas:
        num_moedas = int(round(n, 2) // moeda)
        n -= num_moedas * moeda
        print(f"{num_moedas} moeda(s) de R$ {moeda:.2f}")

# Exemplo de uso:
n = float(input("Insira valor: "))
decomporValor(n)