"""
Set Comprehension

    set = {} - Não guarda valores repetido e nem são ordenados

"""

# Exemplos

# 1
numeros = {num for num in range(1, 7)}
print(numeros)
print('\n')

# 2
quadrado = {x ** 2 for x in range(10)}
print(quadrado)
print('\n')

# Desafio - Faça uma alteração na estrutura acima para gerar um dict:
quadrado_dic = {x: x ** 2 for x in range(10)}
print(quadrado_dic)
print('\n')


# Usando letras
letras = {letra for letra in 'Anderson Peruci'}  # Não irá repetir e nem guardar ordem
print(letras)
