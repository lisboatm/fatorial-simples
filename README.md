# Cálculo do Fatorial

## Descrição

Este programa lê um valor inteiro \( N \) e calcula seu respectivo fatorial. O fatorial de um número \( N \) é definido como o produto de todos os números inteiros de \( N \) até 1. O fatorial é denotado por \( N! \).

A fórmula do fatorial é:

\[ N! = N \times (N - 1) \times (N - 2) \times ... \times 1 \]

### Exemplo

Para um número \( N = 5 \):

\[ 5! = 5 \times 4 \times 3 \times 2 \times 1 = 120 \]

## Requisitos

- O valor de \( N \) deve ser um número inteiro positivo, com a condição de que \( 0 < N < 13 \).

## Entrada

A entrada do programa consiste em uma única linha contendo um valor inteiro \( N \).

```
Entrada:
5
```

## Saída

A saída do programa deve ser um único número inteiro correspondente ao fatorial de \( N \).

```
Saída:
120
```

## Restrições

- O valor de \( N \) deve atender à condição \( 0 < N < 13 \).

## Implementação

O cálculo do fatorial pode ser feito utilizando um laço (loop) ou recursão. Para números pequenos (como no nosso caso, até 12), ambas as abordagens são válidas.

### Exemplo de Código em Python

```python
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Leitura da entrada
N = int(input())
# Cálculo e saída do fatorial
print(fatorial(N))
```

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código acima em um arquivo chamado `fatorial.py`.
3. Execute o arquivo pelo terminal ou prompt de comando:

   ```bash
   python fatorial.py
   ```

4. Insira o valor de \( N \) quando solicitado e pressione Enter.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou reportar problemas.
