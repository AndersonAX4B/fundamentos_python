"""
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False

"""

# Exemplo all()
print(all([0, 1, 2, 3]))  # Lista
print(all((1, 2, 3, 4, 5)))  # Tupla
print(all({1, 2, 3, 4, 5}))  # Set (conjunto)
print(all('1, 2, 3, 4, 5'))  # String
print(all({1: 2, 3: 4}))  # Dict
print(all([]))
print('\n')

# Verificar se o primeiro caracter de todos os itens é igual a C
nomes = ['Carla', 'carlos', 'Cristina', 'cristiano']
print(all([nome[0].upper() == 'C' for nome in nomes]))
print('\n')

# Exemplo any()
print(any([0, False, {}, (), 0, '']))
print(any([0, 1, 2, 3, 4, 5]))  # Lista
print(any((1, 2, 3, 4, 5)))  # Tupla
print(any({1, 2, 3, 4, 5}))  # Set (conjunto)
print(any('1, 2, 3, 4, 5'))  # String
print(any({1: 2, 3: 4}))  # Dict
print(any([]))
print('\n')

# Verificar se o primeiro caracter de todos os itens é igual a C
any_nomes = ['Carla', 'carlos', 'Cristina', 'cristiano', 'daniel']
print(any([nome[0].upper() == 'C' for nome in any_nomes]))
print('\n')

print(all([0, 0, 0, 0, 145, 0, 0]))
print(any([0, 5, 0, 144, 55, 0, 0]))

teste = 'Aqui'
print("A variável " + teste + " é isso")