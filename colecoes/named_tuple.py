"""
Módulo Collections - Named Tuple

link docs Python -> https://docs.python.org/pt-br/3/library/collections.html

# Recapitulando Tupla
Tupla = (1, 2, 3)

Named Tuple -> São tuplas diferenciadas, onde especificamos um nome para a mesma e também parâmetros

"""

# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple
dog = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - Declaração Named Tuple
dog2 = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declaração Named Tuple
dog3 = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Utilizando
# animal = dog(idade=12, raça='Chow-Chow', nome='Rex')
# print(animal)
# animal = dog2(idade=12, raça='Chow-Chow', nome='Rex')
# print(animal)
animal = dog3(idade=12, raça='Chow-Chow', nome='Rex')  # Obrigatório passar todos os parâmetros
print(type(animal))
print(animal)
print('\n')

# Acessando os elementos
# Forma 1
print(animal[0])
print(animal[1])
print(animal[2])
print('\n')

# Forma 2
print(animal.idade)
print(animal.raça)
print(animal.nome)
print('\n')

# Outros métodos
print(animal.index('Rex'))
print(animal.count('Chow-Chow'))
print('\n')


