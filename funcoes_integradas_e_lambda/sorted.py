"""
Sorted

Obs.:
    Não confunda, apesar do nome, com a função sort(), que é aplicado em listas. O sort() só funciona em listas
    Podemos usar o sorted() para qualquer iterável
    Como o próprio nome diz, sorted() é usado pra ordenar
"""

lista = [2, 1, 756, 4, 79, 0, 4]
lista.sort()  # Sort ordena a lista e devolve para ela mesmo! Exclusivo para listas
print(lista)
print('\n')

# Exemplo Sorted
nums = [6, 7, 8, 4, 3, 99, 88, 23]
print(sorted(nums))  # Ordena do menor para o maior. Ele retorna uma nova lista ordenada
print(nums)
print('\n')

# Exemplo 2 - Tupla
tuplas = (6, 7, 8, 4, 3, 99, 88, 23)
print(sorted(tuplas))  # Não importa que foi passado uma tupla, ele retorna uma lista
print(tuplas)
print('\n')

# Adionando parâmetros ao sorted
numeros = [6, 7, 8, 4, 3, 99, 88, 23]
print(sorted(numeros, reverse=True, ))  # Assim, ele ordenará do maior para o menor
print('\n')


# Podemos usar o sorted para coisas mais complexas
# Ordenando um dict
usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje", "Eu sou cachorrão"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]
print(sorted(usuarios, reverse=True, key=lambda username: username['username']))  # Ordenando pelo username
print(sorted(usuarios, key=lambda username: len(username['tweets'])))  # Ordenando pelo quantidade de tweets
print('\n')

estudante_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(estudante_tuples, key=lambda estudante: estudante[2]))  # Ordena pela idade de cada estudante
print('\n')

nome = ['andrea', 'Cristóvão', 'amoedo', 'Anderson', 'Jéssica', 'Eva']
print(sorted(nome, key=len))  # Ordena pelo tamanho de cada item
print('\n')


musicas = [
    {'titulo': 'A', 'executada': 675865656},
    {'titulo': 'B', 'executada': 7587543789},
    {'titulo': 'C', 'executada': 789546879},
    {'titulo': 'D', 'executada': 45786}
]

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, reverse=True,key=lambda musica: musica['executada']))

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['executada']))
