"""
Definindo Funções:
- Funções são pequenos trechos de código que realizam tarefas específicas
- Pode ou não receber entrada de dados e retornar um saída de dados
- Muito úteis para executar procedimentos similares po várias vezes

Conceito para criação de uma função:
- DRY - Don't Repeat Yourself (Não repita você mesmo)


"""
# Exemplo de funções
cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando funções integradas (built-In) do Python
print(cores)
cores.append('roxo')
cores.clear()

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Pytho que estamos definindo uma 
função. Também abrimos o bloco de código com o já conhecido ':' 

Infos:
    nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
    parametros de entrada -> OPCIONAIS, onde tendo mais um, cada um separado por vírgula
    bloco_da_função -> Também chamado de Corpo da função ou implementação, é onde o processamento da função acontece.
        Neste bloco, pode ter ou não retorno da função
    

"""


# Definindo uma função

def dizer_oi():
    print('Oi')
    return 'oi'

dizer_oi()
dizer_oi()
dizer_oi()
dizer_oi()

for _ in range(5):
    dizer_oi()

# Em Python, podemos criar variáveis do tipo de uma função e executar esta função atravpes da variável
falar_oi = dizer_oi  # Não usar o parênteses nesta situação, senão 'falar_oi' receberá o retorno do método

# print(falar_oi)
falar_oi()
