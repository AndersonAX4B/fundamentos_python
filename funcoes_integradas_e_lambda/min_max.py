"""
Min e Max

max() -> retorna o maior valor em um iterável ou o maior de dois ou mais elementos


"""
from datetime import date

# Exemplos - max()
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(lista))
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
print(max(tupla))
conjuntos = {1, 2, 3, 4, 5, 6, 7, 8}
print(max(conjuntos))
dicionarios = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(max(dicionarios))  # Para dict diretamente, ele retorna a chave do maior valor
dicionarios_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(max(dicionarios_values.values()))  # Para dict, usando o values(), ele retorna o maior valor
print('\n')

# Faça um programa que receba dois valores do usuário e mostre o maior
# value1 = int(input('Digite o primeiro valor: '))
# value2 = int(input('Digite o segundo valor: '))
# print(max(value1, value2))
# print('\n')

# Teste
print(max(1, 4, 3, 876, 5456, 3, 2, 0))
print(max('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 't', 'j', 'z'))
print(max('a', 'ab', 'abc', 'abcd'))
print(max(1.9, 4, 3.7878878, 876, 5456, 3.80000009, 2, 0))
print(max('Anderson Peruci'))
print('\n')
print('\n')

# Exemplos - min()
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(min(lista))
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
print(min(tupla))
conjuntos = {1, 2, 3, 4, 5, 6, 7, 8}
print(min(conjuntos))
dicionarios = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(min(dicionarios))  # Para dict diretamente, ele retorna a chave do maior valor
dicionarios_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(min(dicionarios_values.values()))  # Para dict, usando o values(), ele retorna o maior valor
print('\n')

# Faça um programa que receba dois valores do usuário e mostre o maior
# value1 = int(input('Digite o primeiro valor: '))
# value2 = int(input('Digite o segundo valor: '))
# print(min(value1, value2))
# print('\n')

# Teste
print(min(1, 4, 3, 876, 5456, 3, 2, 0))
print(min('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 't', 'j', 'z'))
print(min('a', 'ab', 'abc', 'abcd'))
print(min(1.9, 4, 3.7878878, 876, 5456, 3.80000009, 2, 1.08956767))
print(min('Anderson Peruci'))


# Outros exemplos
nomes = ['Anderson', 'Letícia', 'Wesley', 'Cristovaldo', 'Eva', 'Dora']
print(min(nomes))  # Ele se baseia pela inicial das palavras. Se forem iguais, ele olhará as seguintes
print(max(nomes))
print('\n')

# Ordenar pelo tamanho da palavra
print(min(nomes, key=lambda nome: len(nome)))
print(max(nomes, key=lambda nome: len(nome)))

#
musicas = [
    {'titulo': 'A', 'executada': 675865656},
    {'titulo': 'B', 'executada': 7587543789},
    {'titulo': 'C', 'executada': 789546879},
    {'titulo': 'D', 'executada': 45786}
]
print(min(musicas, key=lambda musica: musica['executada']))
print(max(musicas, key=lambda musica: musica['executada']))

# DESAFIO! Imprima somente o título da música e mais e menos tocada
print(min(musicas, key=lambda musica: musica['executada'])['titulo'])
print(max(musicas, key=lambda musica: musica['executada'])['titulo'])
