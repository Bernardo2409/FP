import random

# Número de amostras a serem geradas
num_amostras = 100000

# Contador para pontos nas áreas ímpares
pontos_impar = 0

# Gerar amostras aleatórias
for _ in range(num_amostras):
    # Gerar um ponto aleatório
    # Vamos mapear as áreas ímpares e pares para um intervalo 0 a 8.
    ponto = random.uniform(0, 4)
    
    # Verificar se o ponto está na área ímpar
    # As áreas ímpares são [0, 2.5) e [3.5, 6) (em relação à área total de 8)
    if (0 <= ponto < 2.5) :
        pontos_impar += 1

# Calcular a probabilidade de cair em uma área ímpar
probabilidade = pontos_impar / num_amostras
print(f"A probabilidade de cair em uma área ímpar é: {probabilidade}")
