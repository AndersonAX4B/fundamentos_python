"""
List Comprehension - 2

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension

"""

# Exemplos

# 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

