values = []

for _ in range(10):
    values.append(int(input('Digite um valor inteiro: ')))

print(max(values))
print(values.index(max(values)))