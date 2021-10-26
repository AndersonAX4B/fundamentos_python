values = []
soma = 0
for _ in range(8):
    values.append(float(input("Digite valores reais: ")))

for cont in range(2):
    soma += values[int(input(f'Digite a {cont + 1} posição: '))]

print(soma)
