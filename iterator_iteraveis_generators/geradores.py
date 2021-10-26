"""
Geradores

 - Geradores (Generators) são Iterators

Infos:
    - Generators podem ser criados com funções geradoras:
        - Funções geradoras utilizam a palavra reservada yield
    -Generators podem ser criados com Expressões Geradoras

Diferença entre função e função geradora (Generator Function):

-----------------------------------------------------------------------------------
| Funções                                 | Generator Functions                   |
-----------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                        |
-----------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield múltiplas vezes  |
-----------------------------------------------------------------------------------
| quando executada, retorna um valor      | quanto executada, retorna um generator|
-----------------------------------------------------------------------------------
"""


# Exemplo de Função Geradora (Generator function)
def conta_ate(max_value):
    contador = 1
    while contador <= max_value:
        yield contador
        contador = contador + 1


# Obs.: Um Generator Funciton não é um Generator. Ela gera um generator

gen = conta_ate(5)

print(type(gen))
print(next(gen))
print(next(gen))
print('\n')

for n in gen:  # Ele continuará a sequência dos número, pois já chamamos o next() anteriormente
    print(n)

# Gerando todos os valores
lista = list(conta_ate(5))
print(lista)
