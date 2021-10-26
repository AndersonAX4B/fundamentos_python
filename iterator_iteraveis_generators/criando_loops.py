"""
Criando a própria versão de Loops

"""


def meu_loop(iteravel):
    it = iter(iteravel)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_loop('Anderson')
