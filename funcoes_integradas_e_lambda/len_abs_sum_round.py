"""
Len, abs, sum e round

# len()
    - Retorna o tamanho, ou seja, o número de itens de um iterável

# abs()
    - Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal
    - Ele 'transforma' negativo em positivo. Ele basicamente remove o sinal matemático do valor
    - Não se aplica a string

# sum()
    - Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
        incluindo o valor inicial
    - O valor inicial default é 0(zero)

# round()
    - Retorna um número arredondado para n digitos de precisão após a casa decimal. Se a precisão não for informada,
        retorna o inteiro mais próximo da entrada
"""

# Exemplo len()
print(len('Anderson Peruci'))
print(len((1, 2, 3, 4, 5, 6)))
print(len([1, 2, 3, 4, 5, 6]))
print(len({1, 2, 3, 4, 5, 6}))
print(len({'a': 1, 'b': 2, 'c': 3}))
print('\n')

# Pode debaixo dos panos
# Dunder len
print('Anderson Peruci'.__len__())
print('\n')

# Exemplo abs()
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
print('\n')

# Exemplo sum()
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1, 2, 3, 4, 5], -95))
print(sum({1, 2, 3, 4, 5}))
print(sum((1, 2, 3, 4, 5)))
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))
print('\n')

# Exemplo round()
print(round(-3.14))
print(round(-2.978874, 3))
print(round(-5))
print(round(10.5))
print(round(10.6))
print(round(10.51))
print(round(10.1287649282732, 5))

print('\n')
