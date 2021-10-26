"""
Dictionary

Dicionários são coleções do tipo chave/valor

Dicionários são representados por {}

- Sobre Dict
-- Tanto chave quanto valor podem ser de qualquer tipo de dado
-- Podemos misturar tipos de dados
-- Qualquer tipo de dado pode ser usado como chave de dicionário

"""

# Declarando um dict
estados_ddd = {11: 'São Paulo', 24: 'Rio de Janeiro', 40: 'Ceará'}
print(estados_ddd)
print(type(estados_ddd))
print('\n')

# Acessando elementos
print(estados_ddd[11])
# print(estados_ddd[645])

print(estados_ddd.get(24))
print(estados_ddd.get(645))

estado = estados_ddd.get(6777, 'Não encontrado')
print(estado)
print('\n')

# Verificar se determinada chave se encontra no Dicionário
print(11 in estados_ddd)
print('São Paulo' in estados_ddd)
print('\n')

# Adicionando novos elementos em um dicionário
# 1
estados_ddd[45] = 'Amazonas'
print(estados_ddd)
print('\n')

# 2
novo_dado = {00: 'Santa Catarina'}
estados_ddd.update(novo_dado)
print(estados_ddd)
print('\n')

# Atualizando valores em um dicionário
# 1
estados_ddd[45] = 'Piauí'
print(estados_ddd)
print('\n')

# 2
estados_ddd.update({00: 'Rio Grande do Sul'})
print(estados_ddd)
# OBS.: Adicionar ou atualizar elementos em um dicionário é a mesma
# OBS.: Em dicionário, NÂO podemos ter chaves repetidas
print('\n')

# Remover dados de um dicionário
# 1
# Sempre informar a chave
# O valor a ser removido, será retornado
estados_ddd.pop(00)
print(estados_ddd)
print('\n')

# 2
# Não retorna o valor removido
del estados_ddd[45]
print(estados_ddd)
print('\n')

# Métodos de dicionários
print(dir({}))
print('\n')

dictionary = dict(a=1, b=2, c=3)
print(dictionary)
print('\n')

# Copiar dict de um para outro
# 1 - Deep Copy
novo = dictionary.copy()
novo['d'] = 4
print(dictionary)
print(novo)
print('\n')

# 2 - Shallow Copy
novo2 = dictionary
novo2['d'] = 4
print(dictionary)
print(novo2)
print('\n')

# Limpar dictionary
dictionary.clear()
print(dictionary)
print('\n')

# Forma não usual de criar dict
# O método fromkeys() recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor iterável uma chave e irá atribuir um valor a esta chave
outro = {}.fromkeys('chave', 'valor')
outro2 = {}.fromkeys(['chave', 'outra_chave'], 'valor')
outro3 = {}.fromkeys([109], 'valor')
outro4 = {}.fromkeys(['chave', 'outra_chave'], ['valor1', 'valor2'])
outro5 = {}.fromkeys(range(1, 11), '')
print(outro)
print(outro2)
print(outro3)
print(outro4)
print(outro5)
