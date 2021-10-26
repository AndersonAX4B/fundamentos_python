"""
Módulo Collections - Default Dict

link docs Python -> https://docs.python.org/pt-br/3/library/collections.html

Default Dict - Ao criar um dicionário utilizando o Default Dict, nós informamos um valor default, podendo utilizar
um lambda para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar
uma chave que não existe, essa chave será criada e o valor default será atribuído

OBS.: Lambda são funções sem nome que podem ou não receber parâmetros de entrada e retornar valores

"""

dicionario = {'curso': 'TI'}

# Recapitulando Dicts
# print(dicionario)
# print(dicionario['curso'])
# print(dicionario['outro'])  # KeyError - Não existe


# Fazendo o import
from collections import defaultdict

default_dict = defaultdict(lambda: None)

default_dict['curso'] = 'Testando o Default Dict'
print(default_dict)

print(default_dict['outro'])  # Usando o Default Dict, não receberemos erro por não existe a chave solicitada
print(default_dict)

print(default_dict['anderson'])
print(default_dict)
