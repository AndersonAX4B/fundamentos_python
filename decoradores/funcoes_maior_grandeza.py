"""
Funções de Maior Grandeza -  Higher Order Funtions (HOF)

O que isso significa?
 - Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
 resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis
 do tipo de funções nos nossos programas


"""
from random import choice


# Exemplos definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))
print('\n')

"""
Nested Funtions - Funções Aninhadas

- Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions ou
Inner Functions (Funções Internas)

"""


# Exemplo
def cumprimento(pessoa):
    def humor():
        return choice(('E aí, ', 'Suma daqui, ', 'Gosto muito de você, '))

    return humor() + pessoa


# Testando
print(cumprimento('Angelina'))
print(cumprimento('Angela'))
print('\n')


# Retornando funções de outras funções
def me_faz_rir():
    def rir():
        return choice(('HAHAHAHAAHHA', 'KKKKKKKKKKKK', 'RSRSRSRSRS'))
    return rir


# Testando
rindo = me_faz_rir()
print(type(rindo))
print(rindo())
print('\n')


# Inner Functions podem acessar o escopo de funções mais externas
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('HAHAHAHAHAHA', 'RSRSRSRSRSRS', 'KKKKKKKKK'))
        return f'{risada} {pessoa}'
    return dando_risada


# Testando
rindo = faz_me_rir_novamente('Anderson')

print(rindo())
print(rindo())
print(rindo())
