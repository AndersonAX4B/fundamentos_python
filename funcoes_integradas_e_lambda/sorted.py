"""
Sorted

Obs.:
    Não confunda, apesar do nome, com a função sort(), que é aplicado em listas. O sort() só funciona em listas
    Podemos usar o sorted() para qualquer iterável
    Como o próprio nome diz, sorted() é usado pra ordenar
"""

lista = [2, 1,  756,4, 79, 0, 4]
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
print(sorted(usuarios, key=lambda user: len(user['tweets'])))  # Ordenando pelo quantidade de tweets
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
print(sorted(musicas, reverse=True, key=lambda musica: musica['executada']))

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['executada']))

print('\n')

usuarios = [{
    "id": 1,
    "last_name": "Exall",
    "amount": 644.04
}, {
    "id": 2,
    "last_name": "Knatt",
    "amount": 1005.28
}, {
    "id": 3,
    "last_name": "Farthin",
    "amount": 710.99
}, {
    "id": 4,
    "last_name": "Wrathmall",
    "amount": 248.8
}, {
    "id": 5,
    "last_name": "Bleasdille",
    "amount": 488.62
}, {
    "id": 6,
    "last_name": "Bigly",
    "amount": 774.7
}, {
    "id": 7,
    "last_name": "Lemmon",
    "amount": 983.87
}, {
    "id": 8,
    "last_name": "Savege",
    "amount": 583.87
}, {
    "id": 9,
    "last_name": "MacDonell",
    "amount": 183.87
}, {
    "id": 10,
    "last_name": "Purchall",
    "amount": 5983.87
}]


print(sorted(usuarios, reverse=True, key=lambda user: user['amount']))
print('\n')
print(sorted(usuarios, key=lambda user: user['amount']))


# Thyago
print('\n')
print(sorted(usuarios, key=lambda item: item['amount']))
print(sorted(usuarios, key=lambda item: item['amount'], reverse=True))

# Guilherme
print('\n')
print(sorted(usuarios, key=lambda amount : amount['amount']))
print(sorted(usuarios, reverse=True, key=lambda amount : amount['amount']))

# Douglas
print('\n')
print(sorted(usuarios, reverse=True, key=lambda user: user['amount']))
print(sorted(usuarios, key=lambda user: user['amount']))

print('\n')
print(sorted(usuarios, reverse=True, key=lambda i: i["amount"]))
print(sorted(usuarios, key=lambda i: i["amount"]))

print('\n')
print(sorted(usuarios, key=lambda amt: amt['amount']))
