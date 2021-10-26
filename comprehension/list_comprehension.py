"""
Umas das features mais importantes do Python

List Comprehension
    - utilizando List Comprehension, nós podemos gerar novas listas com dados processados a partir de outro iterável

Sintaxe:
    [ dado for in iterável ]
"""

# Exemplo 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
# Ele vai multiplicar cada valor da lista 'Numeros' e criar uma nova lista
nova_lista = [num * 10 for num in numeros]
print(nova_lista)
print('\n')


# Exemplo 2
def quadrado(numero):
    return numero ** 2


quadrado_numeros = [quadrado(numero) for numero in numeros]
print(quadrado_numeros)
print(type(quadrado_numeros))
print('\n')

# Comprehension vs Loop
# Loop
sequencia = [1, 2, 3, 4, 5, 6]
sequencia_dobrada = []

for numero in sequencia:
    sequencia_dobrada.append(numero * 2)

print(sequencia_dobrada)

# Comprehension
print([numero * 2 for numero in sequencia])
print('\n')

# Outros exemplos
# 1
nome = 'Anderson'
print([letra.upper() for letra in nome])

# 2
amigos = ['maria', 'pedro', 'miguel', 'vanessa']
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 11)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5, 6]])
