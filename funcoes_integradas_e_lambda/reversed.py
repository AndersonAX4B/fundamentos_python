"""
Reversed

Obs.: Não confunda com a função reverse(), que se aplica apenas em listas

A função reversed() funciona com qualquer iterável

Sua função é inverter um iterável

A função reversed() retorna um iterável chamado List Reverse Iterator
"""

# Exemplos
lista = [1, 2, 3, 4, 5]

res = reversed(lista)  # Ele gera uma nova lista, não altera a lista como faz o reverse()

print(res)  # Após a primeira utilização, ele limpa o espaço de memória
print(type(res))
print('\n')

# Podemos converter o elemento retornado para Lista, Tupla ou Conjunto
# Lista
print(list(reversed(lista)))
# Tupla
print(tuple(reversed(lista)))
# Set(conjuntos)
print(set(reversed(lista)))  # Set não vem ordenado, pois sabemos que os sets(conjuntos) não guardam ordem
print('\n')

# Podemos iterar sobre o reversed
for item in reversed((1, 2, 3, 4, 5)):
    print(item, end='')
print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Anderson'))))
print('\n')

# De forma mais simples
print('Anderson'[::-1])
print('\n')

# Podemos também utilziar o reversed() para fazer um loop for reverso
for i in reversed(range(0, 10)):
    print(i)
print('\n')

# Apesar que também já vimos como fazer isso utilziando o próprio range()
for i in range(9, 0, -1):
    print(i)
