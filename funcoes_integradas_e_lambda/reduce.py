"""
Reduce

Obs.: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a aprtir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todos os casos,
99% das vezes um loop For é mais legível

Para entender o reduce():

# Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)
[1,2,3,4]
A função reduce(), funciona da seguinte forma:
   Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
   Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.
   Isso é repetido até o final.
   Passo 3: res3 = f(res2, a4)
   .
   .
   .
   Passo n: resn = f(resm , an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)

"""

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros, diferente de map() e filter()
res = reduce(lambda acc, nv: acc * nv, dados)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n

print(res)

usuarios = [{
    "id": 1,
    "last_name": "Exall",
    "amount": 644.04
}, {
    "id": 2,
    "last_name": "Knatt",
    "amount": 1005.28
}, {
    "id": 3,
    "last_name": "Farthin",
    "amount": 710.99
}, {
    "id": 4,
    "last_name": "Wrathmall",
    "amount": 248.8
}, {
    "id": 5,
    "last_name": "Bleasdille",
    "amount": 488.62
}, {
    "id": 6,
    "last_name": "Bigly",
    "amount": 774.7
}, {
    "id": 7,
    "last_name": "Lemmon",
    "amount": 983.87
}, {
    "id": 8,
    "last_name": "Savege",
    "amount": 583.87
}, {
    "id": 9,
    "last_name": "MacDonell",
    "amount": 183.87
}, {
    "id": 10,
    "last_name": "Purchall",
    "amount": 5983.87
}]

# another_value = reduce(lambda acc, nv: {'amount': acc['amount'] + nv['amount']}, usuarios)
# print(another_value)

# another_value = reduce(lambda acc, nv: acc + nv['amount'], usuarios, 0)


# print(another_value)

another_value = reduce(lambda acc, nv: {'amount': acc['amount'] + nv['amount']},
                       [user for user in usuarios if 'amount' in user])

another_value = reduce(lambda acc, nv: {'amount': acc['amount'] + nv['amount'] if 'amount' in nv else 0}, usuarios)

another_value = reduce(lambda acc, nv: {'amount': acc['amount'] + nv['amount']},
                       filter(lambda user: 'amount' in user, usuarios))
another_value = reduce(lambda acc, nv: acc + nv.get('amount', 0), usuarios, 0)
print(another_value)
