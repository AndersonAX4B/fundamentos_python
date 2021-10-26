"""
Tipo Boolean

Álgebra Booleana, criada por George Boole

True ou False

Obs.: Sempre com a inicial maiúscula
"""

ativo = True
print(ativo)
print(type(ativo))
print('\n')

# Operações básicas

# Negação
# Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso. Se o valor for falso, o resultado
# será verdadeiro. OU seja, sempre o contrário
print(not ativo)
print('\n')

# Or
# É uma operação binário, ou seja, depende de dois valores. Um ou outro deve ser verdadeiro
print(True or False)
print(True or True)
print(False or False)
print('\n')

# E (and)
# É uma operação binário, ou seja, depende de dois valores. Ambos os valroes devem ser verdadeiros
print(True and False)
print(True and True)
print(False and False)

print(dir(bool))
