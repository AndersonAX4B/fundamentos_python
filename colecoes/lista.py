"""
Lists
Lists in Python working as dynamic vector/matrix and accept any kind of data

- Dynamic: It has no fixed size
- Kind of data: It has no kind of data

- In Python, the list is represented by square brackets: []
"""

lista = [1, "an", 35.3, True]
print(lista[2])

if 3 in lista:
    print("Yes")
else:
    print("Nops")

# /////////////////////////
list2 = list('Anderson')
print(list2)

if "s" in list2:
    print("Yes")
else:
    print("Nops")

# Ordenar item em uma lista
listNum = [1, 54, 65, 423, 4, 5, 6, 876, 0, 28]
listNum.sort()
print(listNum)

# Contar itens em uma lista
listNum = [1, 54, 65, 423, 4, 5, 6, 876, 0, 28, 1, 1, 1, 1, 1]
print(listNum.count(1))
print(listNum.count('e'))

# Adicionar itens em uma lista
# Só podemos adicionar um elemento por vez
listNum = [1, 54, 65, 423, 4, 5, 6, 876, 0, 28, 1, 1, 1, 1, 1, 'e']
listNum.append([32, 34])
print(listNum)

# Adiciona itens individualmente! Não aceita valor único
listNum.extend([123, 456, 789])
print(listNum)

# Adiciona itens em uma posição específica! Não substitui o valor existente
listNum.insert(2, [123, 456, 789])
print(listNum)

# Retorna a lista invertida
listNum.reverse()
print(listNum)
print(listNum[::-1])

# Copiar uma lista
listNum2 = listNum.copy()
listNum3 = listNum
print(listNum2)

# Tamanho da Lista
print(len(listNum))

# remove e retorna o último item da lista
a = listNum.pop()
print(a)
print(listNum)

# remove e retorna item específico da lista
a = listNum.pop(12)
print(a)
print(listNum)

# Limpar a lista
listNum2.clear()
print(listNum2)

# String para lista
# Por padrão ele separa os elementos da lista por espaço
nome = 'Anderson Peruci'
nome = nome.split()
print(nome)

# String para lista usando separador
nome = 'Anderson;Peruci'
nome = nome.split(';')
print(nome)

# Transforma um string em um texto, seprando as palavras por espaço! Só funciona com string
listaNome = ['Meu', 'nome', 'é', 'Anderson']
listaNome = ' '.join(listaNome)
print(listaNome)

# Variáveis dentro da lista
num1 = [0, 1, 1]
num2 = "Peixe"
num3 = True
listVari = [num1, num2, num3]
print(listVari)

# Indexar itens de uma lista
listSec = list(enumerate(listVari))
# for index, item in enumerate(listVari):
#     listSec.extend([(index, item)])
print(listSec)

# Métodos menos importantes

# Em qual indice um valor se encontra
numeros = [1, 2, 3, 4, 5, 6, 7]
print(numeros.index(4))

# Buscando em um range
print(numeros.index(4, 2, 5))

# Usando slice
# lista[inicio:fim:passo]
# range(inicio:fim:passo)
print(numeros[1:])  # Partindo da casa 1 e indo até o final
print(numeros[:3:2])  # Não colando nada, ele não atribui nada
print(numeros[-3:])  # Pegar os últimos elementos da lista
print(numeros[::-1])  # Lista de traz para frente

# Somar, valor máximo, valor mínimo, tamanho
# A lista deve ter somente valores inteiros ou reais
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))

# Converter lista em Tupla
tupla = tuple(numeros)
print(type(tupla))
print(tupla)

# Desempacotando lista
listaDesem = [1, 'uhull', True]
v1, v2, v3 = listaDesem
print(v1)
print(v2)
print(v3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Copy - Gera lista independentes, isso é chamado de Deep Copy
listaDeepy = [1, 2, 3, 4]
novaListaDeepy = listaDeepy.copy()
print(listaDeepy)
novaListaDeepy.append(5)
print(novaListaDeepy)

# Shallow Copy - Uma lista é copiada para a outra, e quando uma sofrer alguma alteração, a outra também sofrerá
listaShallow = [1, 2, 3, 4]

novaListaShallow = listaShallow
print(listaShallow)
print(novaListaShallow)

novaListaShallow.append(5)
print(listaShallow)
print(novaListaShallow)

listatest = [1, 2, 3, 4, 5]
listatest[2] = 9898
print(listatest)

list()

# Verificar se todos itens de uma lista são verdadeiros
verdadeiros = [True, True, True, True]
falsos = [True, False, True, True]
print(all(verdadeiros))
print(all(falsos))

# Retornar a maior data
datas = ['11/12/2020', '13/02/2021', '11/11/1998']
print(max(datas))
