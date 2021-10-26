"""
Documentando funções com Docstrings

Obs.: Podemos ter acesso à documentação de uma função em Python
utilizando a propriedade especial __doc__

"""


def diz_oi():
    """Uma função simples que retorna uma string 'Oi!'"""
    return 'Oi!'


print(diz_oi())
print(help(diz_oi))
print(diz_oi.__doc__)


# Documentado parâmetros
def imprime_dados_usuario(nome, sobrenome, idade=0):
    """
    Função que retorna o nome completo e a idade!

    :param nome: Primeiro nome do usuário.
    :param sobrenome: Sobrenome do usuário.
    :param idade: Idade do usuário. Por padrão é 0.
    :return: Retorna string com nome completo e idade organizados
    """
    return f'{nome} {sobrenome}, {idade}'


print(imprime_dados_usuario('Anderson', 'Peruci', 23))
print(imprime_dados_usuario.__doc__)
