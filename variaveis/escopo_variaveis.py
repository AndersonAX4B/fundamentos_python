"""
Escopo de variáveis
Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
    nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinânima. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.


"""

numero = 42  # Exemplo de variável global
print(numero)
print(type(numero))
print('\n')

numero = 'Geek'
print(numero)
print(type(numero))
print('\n')


nao_existo = 'Oi'
print(nao_existo)
print('\n')


numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto, é local
    print(novo)

print(novo)
print('\n')


# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis loais

nome = 'Anderson'  # Variável global


def imprime_nome():
    nome = 'Ferrari'  # Variável local
    return f'{nome}'


print(imprime_nome())
print(nome)
print('\n')


# Obs.: Se houver uma variável local com o mesmo nome de uma variável global, a local terá preferência

def professor():
    nome_professor = 'Ailton'
    return nome_professor


print(professor())
print('\n')
# print(nome_professor)  # Não é possível usar uma variável local fora do seu scopo

# Outro caso - Errado
# total = 0

# def calcula_total():
#     return  # Só para não estourar erro
#     total = total + 1 # UnboundLocalError: variável local sendo usada sem inicializá-la
#     return total

# print(calcula_total())

# Outro caso - Corrigido
total = 0


def calcula_total():
    global total  # Informando que iremos usar a variável globlal

    total = total + 1
    return total


print(calcula_total())
print('\n')


# Podemos ter funções que são declaradas dentro de outra função
def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador

    return dentro()


print(fora())
