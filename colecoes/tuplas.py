"""
Tuplas

Tuplas em Python são imutáveis, ou seja, não podem ter seus valores alterados após sua criação

As tuplas são representadas por parênteses ()

Métodos de adição e remoção não existem para tuplas

- Por que utilizar tuplas??
-- Tuplas são mais rápidas do que lista;
-- Tuplas deixam seu código mais seguro, devido ao fato de ser imutável
-- Tupla não há Shallow Copy

"""
# As tuplas sçao definidas pelo uso da vírgula, não pelos parênteses
tupla1 = 1, 2, 3, 4, 5
print(type(tupla1))
tupla2 = (2,)
print(type(tupla2))
tupla3 = (2,)
print(type(tupla2))

# Gerando tupla a partir de um range, isso a torna dinâmica
tupla_range = tuple(range(11))
print(tupla_range)

# Desempacotando tupla
tuplaText = ('Anderson', 'Peruci',)
v1, v2 = tuplaText
print(v1)
print(v2)

# Soma*, valor máximo*, valor mínimo* e tamanho
# *Se os valores foram todos inteiros

tupla = (1, 2, 3, 4, 5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla4 = tupla + tupla_range
print(tupla4)

# Tuplas são imutáveis, mas podemos sobrescrever os seus valores
tupla = tupla + tupla_range
print(tupla)

# verificar se o existe um determinado valor na tupla
print(3 in tupla)

# Iterando sobre uma tupla
for v in tupla:
    print(v)
for i, v in enumerate(tupla):
    print(i, v)

# Contando elementos em uma tupla
print(tupla.count(5))

# String para tupla
nome = tuple("Anderson Peruci")
print(nome.count("e"))

# Verifica indice de um item na tupla
print(tupla.index(5))

# Slicing em tuplas
print(tupla[4:8:2])

# Copiando uma tupla para outra
tuplab = tupla
print(tuplab)

# Sobre tuplas
print(help(tupla))



