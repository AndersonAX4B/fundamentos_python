"""
Funções com retorno

Obs.: Em Python, caso a função tem tenha retorno definido, ela retornará 'None'

Obs.: Sobre a palavra reservado 'Return':
    - Ela finaliza a função, ou seja, ela sai da execução da função
    - Podemos ter em uma função, diferentes returns
    - Podemos em uma função, retornar qualquer tipo de dados, até mesmo multiplos valores

"""
from random import random

num = [1, 2, 3]

ret = num.pop()
print(f'Retorno de ret: {ret}')

ret_print = print(num)  # Print não retorna nada, por isso imprime 'None'
print(f'Retorno de print: {ret_print}')


# Exemplo de função com retorno
def quadrado_de_7():
    return 7 * 7


ret_quadrado = quadrado_de_7()
print(ret_quadrado)


def diz_oi():
    return 'Oi, '


nome = 'Anderson'
print(diz_oi() + nome, end='!\n')


# Exemplo 1
def depois_returno():
    print('Antes')
    return 'Return'  # Ela finaliza a função, ou seja, ela sai da execução da função
    print('Depois')


print(depois_returno())


# Exemplo 2
def nova_function():  # Podemos ter em uma função, diferentes returns
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 1


print(nova_function())


# Exemplo 3
def outra_function():
    return 1, 2, 3, 4  # Podemos em uma função, retornar qualquer tipo de dados, até mesmo multiplos valores


n1, n2, n3, n4 = outra_function()
print(n1, n2, n3, n4)
print(outra_function())


# Vamos criar uma função para jogar a moeda:
def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    return 'Cara' if random() > 0.5 else 'Coroa'


print(joga_moeda())
