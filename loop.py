nome = 'Anderson'
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = range(1, 10)

# **********************************
# for n in nome:
#     print(n)
#
# for l in lista:
#     print(l)
#
# for n in numeros:
#     print(n)
#
# for n in range(1, 20):
#     print(n)

# **********************************
for valor in enumerate(nome):
    print(valor)
print('\n')
for indice, _ in enumerate(nome):
    print(indice)
print('\n')
for _, letra in enumerate(nome):
    print(letra)

# ********************************** Emoji
print('\U0001F60D' * 10)

