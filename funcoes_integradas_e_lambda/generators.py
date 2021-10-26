"""
Generators ou Generator Expression

Em aulas anteriores nós estudamos:
    - List Comprehension
    - Dictionary Comprehension
    - Set Comprehension

Não vimos:
    - Tuple Comprehension... porque elas se chamam Generators

"""
# Exemplo
# Retorna true se começar com 'C', senão False
any_nomes = ['Carla', 'carlos', 'Cristina', 'cristiano', 'daniel']
res = (nome[0].upper() == 'C' for nome in any_nomes)
print(type(res))
print(list(res))
print(list(res))  # Como o map e o filter, uma vez usado ele esvaziará o espaço de memória
print('\n')

# Comparação com List Comprehension
# List Comprehension
res_list = [nome[0].upper() == 'C' for nome in any_nomes]
print(type(res_list))

# Generator
res_gen = (nome[0].upper() == 'C' for nome in any_nomes)
print(type(res_gen))
print('\n')

# Por que usar Generator ao invés do List Comprehension?
#   Generator usa menos recurso na memória, com sua aplicação ficará mais performática
#   Quando executado, o Generator armazena apenas uma expressão, ao contrário do List Comprehension
print(res_list)
print(res_gen)
# Exemplo de melhor utilização:
# Usar Generator quando você precisar fazer apenas uma validação dos dados e depois nunca mais usar,
#   como por exemplo na linha 50, pois ele apagará após o uso
# Usar List Comprehension quando você precisar persistir os dados
# Todas as comparações também se aplicam ao dict comprehension e set comprehension

# Verificar se o primeiro caracter de todos os itens é igual a C
any_nomes = ['Carla', 'carlos', 'Cristina', 'cristiano', 'daniel']
print(any(nome[0].upper() == 'C' for nome in any_nomes))
print('\n')


# Outro exemplo
# Método getsizeof()? ->  Retorna a quantidade de bytes em meória do elemento passado como parâmetro

from sys import getsizeof  # isso é para teste, deve ser importado no início do arquivo

# Mostra quantos bytes a string está ocupando em memória. Quanto maior a stirng, maior o espaço usado

print(getsizeof('Anderson'))
print(getsizeof(1))
print(getsizeof(4668795648964598))
print(getsizeof(True))
print('\n')

# Comparando o tamanho do List Comprehension com Generator

# Gerando um lista com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um conjunto com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando um dict com dict comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando um lista com Generator
gen = getsizeof(x * 10 for x in range(1000))

print(list_comp)
print(set_comp)
print(dict_comp)
print(gen)
print('\n')


# Iterando Generator
iterar_gen = (x * 10 for x in range(7))
print(iterar_gen)
for iteravel in iterar_gen:
    print(iteravel)

