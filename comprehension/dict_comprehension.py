"""
Dictionary Comprehension

Pense o seguinte;

    Se quisermos criar uma lista fazemos;
        lista = [1, 2, 3]

    Se quisermos criar um uma tupla:
        tupla = (1, 2, 3)  # Ou tuple = 1, 2, 3

    Se quisermos criar um set (Conjunto):
        conjunto = {1, 2, 3}

    Se quisermos criar um dicionário:
        dicionario = {'a': 1, 'b': 2, 'c': 3}

# Sintaxe do Dictionary Comprehension
    {chave:valor for valor in iterável}

"""

# Exemplos
# 1
dicionario = {'a': 1, 'b': 2, 'c': 3}
quadrado = {chave: valor ** 2 for chave, valor in dicionario.items()}
print(quadrado)
print('\n')

# 2
numeros = [1, 2, 3, 4]
dict_quadrado = {valor: valor ** 2 for valor in
                 numeros}  # Lembrando que dict não pode ter chave duplicada, ele substituirá o valor
print(dict_quadrado)
print('\n')

# 3
chaves = ('a', 'b', 'c', 'd')
valores = [1, 2, 3, 4]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# 4 - Exemploc com lógioca condicional
numbers = [1, 2, 3, 4, 5]
retorno = {num: ('par' if num % 2 == 0 else 'impar') for num in numbers}
print(retorno)
