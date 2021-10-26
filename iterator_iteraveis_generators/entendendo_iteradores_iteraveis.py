"""
Enetendendo Iterators e Iterables

Qual é a diferença de um iterador para um iterável?

Iterator:
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada

"""

nome = 'HAHA'  # É um iterable, mas não é um iterador
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable, mas não um iterador

iter1 = iter(nome)  # Transforma o iterable em um iterator para que possa ser iterável
iter2 = iter(numeros)

print(type(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print('\n')
# print(next(iter1))  # Ele retornar um erro dizendo que o iterator já acabou


for letra in nome:
    print(letra)
