# Exemplo mais complexo
usuarios = {
    "name": 'Zé',
    "child_ids": [
        {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"], 'idade': 24},
        {"username": "carla", "tweets": ["Eu amo meu gato"], 'idade': 17},
        {"username": "jeff", "tweets": [], 'idade': 34},
        {"username": "bob123", "tweets": [], 'idade': 18},
        {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"], 'idade': 45},
        {"username": "gal", "tweets": [], 'idade': 37}
    ]
}
print(usuarios)
# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
# Forma 2
ativos = list(filter(lambda usuario: usuario['tweets'], usuarios['child_ids']))
print(ativos)
