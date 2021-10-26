"""
Módulo Collections - Deque

link docs Python -> https://docs.python.org/pt-br/3/library/collections.html

Podemos dizer que deque é uma lista de alta de performance

"""

# Importando
from collections import deque

deq = deque('Anderson')
print(deq)
print(type(deq))
print('\n')

# Adicionando elementos no deque
deq.append('s')  # Adiciona o elemento ao final da lista
print(deq)
print('\n')

deq.appendleft('s')  # Adiciona o elemento no início da lista
print(deq)
print('\n')

# Removendo elementos
deq.pop()  # Remove e retorna o último elemento da lista
print(deq)
print('\n')

deq.popleft()  # Remove e retorna o primeiro elemento da lista
print(deq)
