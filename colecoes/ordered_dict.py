"""
Módulo Collection - Ordered Dict

link docs Python -> https://docs.python.org/pt-br/3/library/collections.html

*Em um dicionário, a ordem dos elementos não é garatida, os elementos podem ser retornado desordendos

Usando o Ordered Dict, teremos a certeza que ele manterá a ordem do dicionário

OrderedDict -> É um dicionário, nos garante a ordem de inserção dos elementos
"""
from collections import OrderedDict

estados_ddd = OrderedDict({11: 'São Paulo', 24: 'Rio de Janeiro', 40: 'Ceará', 10: 'Pernambuco'})
print(type(estados_ddd))
print(estados_ddd)
print('\n')

for key, value in estados_ddd.items():
    print(f'chave={key}:valor={value}')
print('\n')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
# São Iguais?
print(dict1 == dict2)  # True -> Já que ordem dos elementos não importa para o dicionário comum
print('\n')

# Dicionários usando o Ordered Dict
dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'b': 2, 'a': 1})
# São Iguais?
print(dict3 == dict4)  # False -> Com o OrderedDict os elementos passam a ter posição e isso os diferenciam
