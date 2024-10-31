# Leitura do valor N
N = int(input())

# Inicializando a variável que armazenará o fatorial
fatorial = 1

# Cálculo do fatorial
for i in range(1, N + 1):
    fatorial *= i  # Multiplicando fatorial pelo próximo número

# Impressão do resultado
print(fatorial)
