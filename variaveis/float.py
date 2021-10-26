"""
Tipo Float

Tipo Real ou decimal

Número com casas decimais

O separador de casas decimais é o ponto(.), e não a vírgula, exemplo 1.44
"""

decimal = 1.44
print(type(decimal))
print(decimal)
print('\n')


# Convertendo float para inteiro
inteiro = int(1.76)  # Ao converter para inteiro, perdemos a precisão do valor
print(inteiro)
print('\n')

# Arredondar valor float
print(round(inteiro, 1))
print('\n')

# Podemos trabalhar com números complexos
complexo = 5j
print(complexo)
print(type(complexo))

# Na matemática, qualquer número complexo elevado a 2, retorna - 25
print(complexo ** 2)
print('\n')

print(dir(complex))

