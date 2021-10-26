"""
Funções com parâmetro (de Entrada)

- Funções que recebem dados para serem processados dentro da mesma;


"""


def quadrado(numero):
    return numero ** 2


print(quadrado(5))
print(quadrado(7))


def imprime_parabens(aniversariante):
    print('Parabéns para você')
    print('Seja feliz')
    print(f'Feliz aniversário, {aniversariante}')


imprime_parabens('Anderson')


# Podemos ter vários parâmetros
def soma(n1, n2):
    return n1 + n2


def multiplica(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtrai(n1, n2):
    return n1 - n2


print(soma(1, 2))
print(subtrai(2, 1))
print(multiplica(3, 2))
print(divide(4, 2))


# A diferença entre parâmetros e argumentos
# Parâmetros são varáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função

# A ordem dos parâmetros importa

# Argumentos nomeados, conhecidos como Keyword Arguments
# Caso utilizemos nome dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem


def imprime_nome(nome, sobrenome):
    print(f'O nome completo é {nome} {sobrenome}')


imprime_nome('Anderson', 'Peruci')
imprime_nome(sobrenome='Peruci', nome='Anderson')
