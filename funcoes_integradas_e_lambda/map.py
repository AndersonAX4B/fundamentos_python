"""
Map

Com map, fazemos mapeamento de valores para função
"""

import math


def area(raio):
    """Calcula a área de um círculo com raio 'r'"""
    print(raio)
    #return math.pi + (raio ** 2)


raios = [3, 6, 45, 9]
a = [2, 3]

# Forma 2 - Usando Map
# Map uma função que recebe dois parâmetros: O primeiro uma função, o segundo o iterável
# O map está mapeando cada item no iterável e passando para a função
# Geralmento o map é usado com uma expressão Lambda
areas = map(area, raios)
print(areas)
print(type(areas))  # Retorna um tipo próprio
print(list(areas))  #
print('\n')

# Forma 3 - Map com Lambda

res_areas = list(map(lambda raio: math.pi + (raio ** 2), raios))
print(res_areas)
print('\n')

# Obs.: Após utilziar a função map(), depois da primeira utilização, os valores da variável tipo map são zerados
# Exemplo
map_zera = map(lambda raio: math.pi + (raio ** 2), raios)
print(map_zera)
print(list(map_zera))
print(list(map_zera))
print(map_zera)
print('\n')

# map é um iterável
iteravel_map = map(lambda raio: math.pi + (raio ** 2), raios)
for value in iteravel_map:
    print(value)
print('\n')

# Para fixar - Map
# Temos dados iteráveis:
# dados: a1, a2, ..., an
# Temos uma função:
# Função: f(x)
# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.
# O Map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo - Converter a tempratura em Celsius para Fahrenheit

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londes', 22)]

# f = 9/5 * c + 32

# Lambda

print(list(map(lambda dado: (dado[0], (9 / 5) * dado[1] + 32), cidades)))
# A função que for passada ao map, deve receber apenas UM parâmetro
