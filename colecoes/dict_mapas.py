""""
Mapas -> Conhecidos em Python como dicionário

Dicionário são representados por chaves {}
"""
meses = {'jan': 1, 'fev': 2, 'mar': 3}
print(meses)

# Iterar sobre dicionário
for key in meses:
    # Vai imprimir a chave contida no dicionário
    print(key)
print('\n')

for key in meses:
    # Vai imprimir o valor da chave contido no dicionário
    print(meses[key])
print('\n')


# Retorna as chaves do dicionário
print(meses.keys())
print('\n')

# Jeito pythonico para varrer todas as keys do dict
for key in meses.keys():
    # Vai imprimir a chave contida no dicionário
    print(key)
print('\n')

# Jeito pythonico para acessar os valores do dict
print(meses.values())
for values in meses.values():
    #  Vai imprimir o valor da chave contido no dicionário
    print(values)
print('\n')


# Desempacotamento de dicts
print(meses.items())
for key, values in meses.items():
    print(f'{key} : {values}')
print('\n')

# Soma*, Valor Máximo*, Valor Mínimo* e tamanho
# *Se os valores foram inteiros ou reais
print('\n')

print(sum(meses.values()))
print(max(meses.values()))
print(min(meses.values()))
print(len(meses))


