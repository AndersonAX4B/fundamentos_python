"""
Funções com parâmetro Padrão (Default Params)

- Funções onde a passagem de paraâmetro seja opcional

def exponencial(numero, potencia=2):
    return numero ** potencia


Por que utilizar parâmetros com o valor default?
# Nos permite ser mais flexíveis nas funções
# Evita erros com parâmetros incorretos
# Nos permite trabalhar com exemplos mais legíveis de código

Quais tipos de dados podemos utilziar como valores default para parâmetros?
# Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc...


Obs.:
# Se o usuário passar somente 1 argumento, este será atribuído ao parâmetro 'numero'
# Se passar 2 argumentos, amboes parâmeteros serão preenchidos, subistuindo o valor padrão
# Parâmetros sem valor padrão deve ser declarado antes dos parâmetros com valor padrão,
    portanto os párâmetros com valores padrões devem ser criado ao final da declaração

"""


# Exemplo
# Função que calcula a potência de um número. Caso o valor da potência não for passador, ele usará o valor padrão,
# No caso, 2
def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(3, 3))


# Exemplo mais complexo
def mostra_informacao(nome='Anderson', chefe=False):
    if nome == 'Anderson' and chefe:
        return 'Bem vindo, Chefe'
    elif nome == 'Anderson':
        return 'Você é Anderson, mas não é o chefe HAHA'
    return f'Olá, {nome}'


print(mostra_informacao('Carlos', True))
print(mostra_informacao())
print(mostra_informacao(chefe=True))


# Exemplos com parâmetro com valor de funções
def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 - numero2


def mat(numero1, numero2, funcao=soma):
    return funcao(numero1, numero2)


print(mat(1, 2))
print(mat(2, 1, subtracao))

# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis loais

nome = 'Anderson'  # Variável global


def imprime_nome():
    nome = 'Ferrari'  # Variável local
    return f'{nome}'


print(imprime_nome())
print(nome)


# Obs.: Se houver uma variável local com o mesmo nome de uma variável global, a local terá preferência

def professor():
    nome_professor = 'Ailton'
    return nome_professor


print(professor())
# print(nome_professor)  # Não é possível usar uma variável local fora do seu scopo

# Outro caso - Errado
# total = 0

# def calcula_total():
#     return  # Só para não estourar erro
#     total = total + 1 # UnboundLocalError: variável local sendo usada sem iniciualizá-la
#     return total

# print(calcula_total())

# Outro caso - Corrigido
total = 0


def calcula_total():
    global total  # Informando que iremos usar a variável globlal

    total = total + 1
    return total


print(calcula_total())


# Podemos ter funções que são declaradas dentro de outra função

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador

    return dentro()


print(fora())
