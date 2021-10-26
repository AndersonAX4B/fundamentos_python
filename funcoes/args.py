"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que começe como asterisco. Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?
# O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em um tupla.
    Então, desde já lembre-se que tuplas são imutáveis

# OBS.: O parâmetro *args não é obrigatório

"""


# Entendendo o args
# Exemplo
def soma_todos(*args):
    print(sum(args))


soma_todos()
soma_todos(1, 2, 3, 4, 5)
soma_todos(1, 3)


# Exemplo - 2
def soma_todos_com_mais_params(nome, sobrenome, *args):
    print(f'Nome: {nome}\nSobrenome: {sobrenome}\nSoma: {sum(args)}\n')


soma_todos_com_mais_params('Anderson', 'Peruci')
soma_todos_com_mais_params('Anderson', 'Peruci', 1, 2, 3, 4, 5)
soma_todos_com_mais_params('Anderson', 'Peruci', 1, 3)


# Outro exemplo de utilização do *args
def verifica_info(*args):
    if 'Anderson' in args and 'Peruci' in args:
        return f'Bem-vindo Anderson Peruci'
    return 'Eu não sei quem você é...'


print(verifica_info())
print(verifica_info(1, True, 'Peruci', 'Anderson'))
print(verifica_info(1, 'University', 3.1454))

# Exemplo caso for passado outros tipos de dados para *args - Usando desempacotador automático
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def soma_todos(*args):
    print(f'\n{args}')


soma_todos()
soma_todos(*numeros)
# Usar asterísco para informar ao python que estamos passando como argumento uma coleção de dados,
# desta forma ele saberá que precisará desempacotar estes dados. Usar em caso de tuplas e lista.
