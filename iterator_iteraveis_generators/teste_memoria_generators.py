"""
Teste de memória com Generators

"""


# Sequência de Fibonacci - Função usando Lista - 489MB
def fib_list(qnt_nums):
    nums = []
    a, b, = 0, 1
    while len(nums) < qnt_nums:
        nums.append(b)
        a, b = b, a + b
    return nums


# Testando
# for n in fib_list(100000):
# print(n)


# Usando Geradores - 3MB
def fib_gen(qnt_nums):
    a, b, cont = 0, 1, 0
    while cont < qnt_nums:
        a, b = b, a + b
        yield a
        cont = cont + 1


# Teste 2 Generators
for n in fib_gen(10):
    print(n)
