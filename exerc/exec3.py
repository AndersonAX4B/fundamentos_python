# Leia e imprima a soma de três valores

soma = 0
for n in range(3):
    soma += int(input(f'Digite o valor {n+1}/3: '))
print(soma)
