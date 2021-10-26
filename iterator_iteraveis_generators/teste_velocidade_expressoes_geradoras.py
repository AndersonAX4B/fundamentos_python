"""
Teste de velocidade com Expressões Geradoras

"""
from time import time


# Generators
def nums():
    for num in range(1, 10):
        yield num


gen1 = nums()
print(gen1)
print(next(gen1))
print(next(gen1))
print('\n')

# Generator Expression
gen2 = (num for num in range(1, 10))
print(gen2)
print(next(gen2))
print(next(gen2))
print('\n')

# Exemplo de soma dos valores
print(sum(num for num in range(1, 10)))
print('\n')

# Realizando o teste de velocidade
print('Iniciando soma...')
# Generator Expression
gen_inicio = time()
print(sum(num for num in range(100_000_000)))  # 100 Milhões
gen_tempo_total = time() - gen_inicio

# List Comprehension
list_inicio = time()
print(sum([num for num in range(100_000_000)]))  # 100 Milhões
list_tempo_total = time() - list_inicio

# Imprimindo ambos tempos
print(f'Generator Expresion demorou: {gen_tempo_total}')
print(f'List Comprehension demorou: {list_tempo_total}')
