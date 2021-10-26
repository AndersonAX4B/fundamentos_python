"""
Tipo String

Em Python, um dado é considerado string sempre que:
    - Estiver entre apóstrofo, apóstrofo triplo, aspas ou aspas triplas -> 'Anderson', "23", '''323.4'''
    

"""
# print(help(str))
# print(dir(str))




nome = 'Anderson'
sobrenome = "Peruci"
descrição = ''' Alguém que anda pra frente
Ou anda para trás'''
descricao2 = """ Vai para direita
ou esquerda"""

print(nome)
print('\n')
print(sobrenome)
print('\n')
print(descrição)
print('\n')
print(descricao2)
print('\n')

# Pulando linha
nome_completo = 'Anderson \nPeruci'
print(nome_completo)
print('\n')

# Caracter de escape
escape = "Anderson \" Peruci"
print(escape)
print('\n')

# Transformar tudo em maiúsculo
maiusculo = 'tudo maiúsculo'
print(maiusculo.upper())

# Transformar tudo em minúsculo
maiusculo = 'TUDO MINÚSCULO'
print(maiusculo.lower())
print('\n')


# Transforma em lista de strings
quebrar = 'Quebrando tudo'
print(quebrar.split())  # Por padrão ele quebra por espaço
print('\n')

quebrar = 'Quebrando;tudo'
print(quebrar.split(sep=';'))
print('\n')

# Imprimindo uma determinada parte da string
determinado = 'Anderson Peruci'
print(determinado[4])
print('\n')
# Ou
print(determinado[0:4])  # Slice de string
print('\n')
# Ou
print(determinado.split()[0])
print('\n')

# Inverter uma string
inverso = 'Anderson Peruci'
print(inverso[::-1])
print('\n')


# Substituir letras de uma string
subs = 'Anderson'
print(subs.replace('A', 'E'))  # Se houver repetidos, ele irá replicar
print('\n')


# Encontrando caractere em uma string
encontrando = 'Achou aqui'
print(encontrando.find('qui'))
print('\n')

# Removendo espaços iniciais e finais em branco em uma string
espaco = ' remove incio e fim '
print(espaco.strip())
print('\n')
