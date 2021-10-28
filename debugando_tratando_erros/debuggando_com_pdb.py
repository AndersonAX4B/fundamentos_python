"""
Debuggando com PDB

PDB - Python Debugger
"""
# Exemplo de debug com o PDB

# Para utilizar o Python Debbuger, precisamos importar a biblioteca pdb e então utilizar a função set_trace()
# Comando básicos do PDB
# l - Listar onde estamos no código
# n - Próxima instrução
# p - Imprimir variável
# c - Continuar a execução (Finaliza o debugger)

# --------------------- 1
import pdb

nome = 'Anderson'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = 'Anderson Peruci'
curso = 'Programação em Python'
final = nome_completo + ' faz ' + curso
print(final)

# --------------------- 2
# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento! Costumamos realizar todos os imports de libs no início do arquivo.
# Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somento onde vamos debbugar,
# E o finalizar já fazemos a remoção, assim não esquecendo imports ou linhas inúteis no código

nome = 'Anderson'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # Uso do ; serve para incluir mais de um comando na mesma linha
nome_completo = 'Anderson Peruci'
curso = 'Programação em Python'
final = nome_completo + ' faz ' + curso
print(final)


# --------------------- 3
# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado
# como função built-in (integrada) chamada breakpoint()

nome = 'Anderson'
sobrenome = 'Jolie'
breakpoint()
nome_completo = 'Anderson Peruci'
curso = 'Programação em Python'
final = nome_completo + ' faz ' + curso
print(final)