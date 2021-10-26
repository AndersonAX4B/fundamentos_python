"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas

# Função normal em Pyhton
    def soma(x):
        return 3 * x + 1

# Expressão Lambda
    lambda x: 3 * x + 1
"""

# Exemplo 1
# lambda x: 3 * x + 1  # Não é possível utilizá-la se declarada deste jeito

# Como usá-la
# calc = lambda x: 3 * x + 1  # Não é forma comum que lambda será usada, mas há possibilidade
# print(calc(4))


# Podemos ter expressões lambdas com múltiplas entradas
# Obs.: Não podemos passar mais argumento do que os parâmetro esperados
#  lambda x, y, z: 3 * x + y / z + 1

# Outro Exemplo - Ordenando pelo sobrenome
jogadores = ['Ronaldinho Gaúcho', 'Neymar da Silva Júnior', 'Cristiano Pereira Ronaldo', 'Ronaldo Fenômeno',
             'Emerson Arantes do nascimento', 'Paulo Henrique Ganso', 'D. Backham Figueiredo', 'L. Messi da Silva']

jogadores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(jogadores)
print('\n')


# Função quadrática
# f(x) = a * x ** 2 + b * x + c
# Defindo a função
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


funcao_quadratica = geradora_funcao_quadratica(2, 3, -5)
print(funcao_quadratica(0))
print(funcao_quadratica(1))
print(funcao_quadratica(2))
print('\n')
# Ou
funcao_quadratica_res = geradora_funcao_quadratica(3, 0, 1)(2)
print(funcao_quadratica_res)
