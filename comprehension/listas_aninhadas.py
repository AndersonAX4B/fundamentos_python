"""
Listas Aninhadas (Nested Lists) - Muito usado em AI, games, Data Science...

- Algumas linguagens de programação (C / Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays / vetores)
    - Multidimensionais (Matrizes)

- Em Python nós temos as listas, que são similares aos arrays/vetores:
    num = [1, 2, 3, 4]

- Em Python nós temos as listas ainhadas, que são similares as matrizes:
    num = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  # Matriz 3x3

"""

# Exemplo 1
num = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]  # Matriz 3x3
print(num)
print(type(num))
print('\n')

# Como fazemos para acessar os dados?
print(num[0])
print(num[0][0])
print('\n')

# Iterando com loops em uma lista aninhada
for numero in num:
    for n in numero:
        print(n)

print('\n')

# Usar list comprehension
[[print(valor) for valor in numero] for numero in num]
print('\n')


# Outros Exemplos
# Gerando uma matriz 3x3
matriz = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(matriz)
print('\n')


# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
print('\n')
