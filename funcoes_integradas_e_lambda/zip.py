"""
Zip

# zip()
    -  Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entradas em pares
    - ele usará cada elemento das listas passadas pra gerar novas listas, juntando os elementos de cada posição
"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

zip1 = zip(lista1, lista2, lista3)

print(zip1)
print(list(zip1))  # Após usado, ele limpará o espaço de memória
print(type(zip1))
print('\n')

# Podemos gerar um lista, tupla, set(conjuntos) ou dicts
print(list(zip(lista1, lista2)))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip(lista1, lista2)))  # Para dict, não é possível passar 3 parâmetros
print('\n')

# Outro exemplo
# Obs.: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso siginifica que se estiver trabalhando com
# iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar
l1 = [1, 2, 3]
l2 = [4, 5, 6, 66]
l3 = [7, 8, 9, 10, 11]
print(list(zip(l1, l2, l3)))
print('\n')

# Podemos utilizar diferentes iteráveis com zip
tupla = (1, 2, 3)
lista = [1, 2, 3]
dicts = {'a': 1, 'b': 2, 'c': 3}
zt = zip(tupla, lista, dicts.values())
print(list(zt))
print('\n')

# lista de tuplas
dados = [(0, 1), (2, 3), (4, 5), (6, 7)]
print(*dados)
print(list(zip(*dados)))
print('\n')

# Mais complexo
# Gerar uma lista com o aluno e sua maior nota
p1 = [80, 91, 78]
p2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']
# print(list(zip(alunos, p1, p2)))

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, p1, p2)}
print(final)

# Podemos usar o map para resolver
final = zip(alunos, map(lambda nota: max(nota), zip(p1, p2)))
print(dict(final))
