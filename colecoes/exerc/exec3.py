values = []
quadrado = []

for cont in range(10):
    value = float(input('Digite um número real: '))
    values.append(value)
    quadrado.append(value*value)

print(f'Valores: {values}')
print(f'Quadrado dos valores: {quadrado}')
