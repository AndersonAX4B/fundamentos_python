"""
Decorators com diferentes assinaturas

- Caso queira passar dois parâmetros para uma funções decoradora e ela só aceita 1 parâmetro, usamos Decorator Pattern
    para resolver esse problema


A assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada
"""


# Reforçando
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou {nome}'


# print(saudacao('anderson', 'Peruci'))
print(saudacao('anderson'))
print('\n')


# Refatorando com o Decorator Pattern
def maiusculo(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@maiusculo
def bom_dia(nome):
    return f'Olá, eu sou {nome}'


@maiusculo
def pedido(principal, acompanhamento):
    return f'Olá eu gostaria de {principal} acompnhado de {acompanhamento}, por favor'


@maiusculo
def lol():
    return 'lol'


print(bom_dia('Anderson'))
print(pedido('Peixo cozido', 'Brócolis'))
print(pedido(acompanhamento='Peixo cozido', principal='Brócolis'))
print(lol())
print('\n')


# Testando
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra_interna(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra_interna
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(comida_favorita('pizza', 'macarronada'))
print(comida_favorita('macarronada', 'pizza'))
print('\n')
print(soma_dez(10, 11))
print(soma_dez(11, 10))
print('\n')
