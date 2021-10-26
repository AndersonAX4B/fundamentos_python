"""
**kwargs

Poderíamos chamar esse parâmetro de qualquer coisa, como por exemplo **nomes,
    mas por convenção, utilizamos **kwargs para definí-lo

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tuplas, o **kwargs exige
    que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário

# OBS.: Os parâmetros *args e **kwargs não são obrigatórios

# Ordem dos parâmetros das funções
 - Parâmetros obrigatórios
 - *args
 - Parâmetros default
 - **kwargs

"""


# Exemplo 1
def cores_favoritas(**kwargs):
    for person, color in kwargs.items():
        print(f'A cor favorita de {person.title()} é {color}')


cores_favoritas(anderson='Azul', ze='Branco')


# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if 'anderson' in kwargs and kwargs['anderson'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'anderson' in kwargs:
        return f"{kwargs['anderson']} Anderson!"
    return 'Não tenho certeza de quem você é...'


print(f'\n{cumprimento_especial()}')
print(cumprimento_especial(anderson='Python'))
print(cumprimento_especial(anderson='Oi'))
print(cumprimento_especial(anderson='especial'))
print(cumprimento_especial(params=None))


# Exemplo usando todos os tipos de parâmetros
def minha_funcao(idade, nome, *args, solteiro=True, **kwargs):
    print('\n')
    print(f'{nome.title()} tem {idade} anos')
    print(args)
    print('Solteiro' if solteiro else 'Casado')
    print(kwargs)


minha_funcao(23, 'anderson')
minha_funcao(21, 'marcela')
minha_funcao(41, 'Marlom', 4, 5, 6, solteiro=False)
minha_funcao(54, 'Ellen', indigena=False, vai=True)
minha_funcao(15, 'Carla', 9, 45, 4, python=True, menor=True)


# Declaração incorreta de parâmetros
def info(a, b, c='Anderson', *args, **kwargs):
    return [a, b, args, c, kwargs]


print('\n')
print(info(1, 2, 3, sobrenome='peruci', cargo='dev'))


# Declaração correta
def info(a, b, *args, c='Anderson', **kwargs):
    return [a, b, args, c, kwargs]


print('\n')
print(info(1, 2, 3, sobrenome='peruci', cargo='dev', ))


# Desempacotando com **kwargs
def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nome = {'nome': 'Anderson', 'sobrenome': 'Peruci'}
print('\n')
print(mostra_nome(**nome))


# Desempacotando parâmetros da função
def soma_valores(a, b, c):
    print(a)
    print(b)
    print(c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)  # Ou
# dicionario = {'a': 1, 'b': 2, 'c': 3}

print('\n')
soma_valores(*lista)
soma_valores(*tupla)
soma_valores(*conjunto)
soma_valores(**dicionario)

# Obs.: Os nomes da chave do dicionário devem ser os mesmos dos nomes dos parâmetros da função
