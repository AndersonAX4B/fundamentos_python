"""
Teoria dos conjuntos da matemática

É a teoria matemática capaz de agrupar elementos

https://www.todamateria.com.br/teoria-dos-conjuntos/

No Python, os conjuntos são chamados de 'Sets'

Da mesma forma que na matemática:
    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utiliziar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles
 Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjunto (Sets) e Dicionários (Mapas) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor.

Além de não termos valores duplicados, não temos ordem

"""

# Definindo um conjunto
# 1
conjunto = set({1, 2, 3, 4, 5, 6, 1, 2, 3, 4})
print(conjunto)
print(type(conjunto))
# OBS.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro
print('\n')

# 2 - Mais comum
conj = {1, 2, 3, 4, 5, 6, 6}
print(conj)
print(type(conj))
print('\n')

text = set('Anderson Peruci')
print(text)
print('\n')

lista = [1, 2, 3, 4, 5, 6, 6]
print(set(lista))
print('\n')

tupla = (1, 2, 3, 4, 5, 6, 6)
print(set(tupla))
print('\n')

# Verificar se existe um determinado elemento no conjunto
if 3 in conjunto:
    print('Tem')
print('\n')

# Exemplificando que conjuntos não tem ordem
lista1 = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista1} - {len(lista1)}')
print('\n')

tupla1 = tuple(lista1)
print(f'Tupla: {tupla1} - {len(tupla1)}')
print('\n')

# Não aceita chaves duplicadas
dicionario = {}.fromkeys(lista1, 'dict')
print(f'Dict: {dicionario} - {len(dicionario)}')
print('\n')
# Não aceita valores duplicados
conjunto_ordem = set(lista1)
print(f'Sets: {conjunto_ordem} - {len(conjunto_ordem)}')
print('\n')

# Assim como todos os outros tipos de dados, podemos colocar tipos de dados misturados nos sets
# Não permite lista, dict e sets dentro do conjunto
test = {1, 'Anderson', True, 32.2, tuple([99, 2]), tuple({'1': '2'}), tuple({1, 2, 3})}
print(test)
print(type(test))
print('\n')

# Iterando um set
for value in test:
    print(value)

print('\n')

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em um feira e os visitantes
# informaram manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar os novos elementos
# E ter repetição
cidades = ['BH', 'SP', 'RJ', 'Curitiba', 'Cuiabá', 'SP', 'Campo Grande', 'RJ', 'BH']
print(cidades)
print(len(cidades))
# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos
# Podemos:
print(len(set(cidades)))
print('\n')

# Adicionando elementos em um conjunto
add_conjunto = {1, 2, 3}

add_conjunto.add(9)
print(add_conjunto)
print('\n')

# Remover elemento em um conjunto
rem_conjunto = {1, 2, 3, 9}

# 1
# Se não encontrar, retorna erro
rem_conjunto.remove(3)  # Indicar o valor a ser removido
print(rem_conjunto)

# 2
# Não retorna erro se não existir
rem_conjunto.discard(2)  # Indicar o valor a ser removido
print(rem_conjunto)
print('\n')

# Copiando um valor para o outro
# 1 - Deep Copy
novo = add_conjunto.copy()
novo.add(4)
print(add_conjunto)
print(novo)

# 2 - Shallow Copy
novo = rem_conjunto
novo.add(4)
print(rem_conjunto)
print(novo)
print('\n')

# Podemos remover todos os itens do conjunto
rem_conjunto.clear()
print(rem_conjunto)
print('\n')

# Métodos Matemáticos de Conjuntos
print('#########################################')
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# Contendo estudantes de Java

estudantes_python = {'Marcos', 'Anderson', 'Ana', 'Marcela', 'Gisele', 'Diego'}
estudantes_java = {'Daniel', 'Anderson', 'Mariana', 'Bianca', 'Gisele', 'Wesley', 'Diego'}
# OBS.: Alguns alunos que estudam Python também estudam Java

# Precisamos gerar um conjunto com nomes de estudantes únicos

# 1 - Utilizando union
unicos = estudantes_python.union(estudantes_java)
print(unicos)

# 2 - Usando o pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
print('\n')

# Gerar um conjunto com estudantes que estão em ambos cursos
# 1 - Utilizando o intersection
ambos = estudantes_python.intersection(estudantes_java)
print(ambos)

# 2 - Utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)
print('\n')

# Gerar um conjunto de estudande que fazem apenas um curso
# 1
apenas_python = estudantes_python.difference(estudantes_java)
print(apenas_python)

apenas_java = estudantes_java.difference(estudantes_python)
print(apenas_java)
print('\n')

# Soma*, Valor Máximo*, Valor mínimo* e tamanho
# * Se os valores forem todos inteiros ou reais
valores = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
print(sum(valores))
print(max(valores))
print(min(valores))
print(len(valores))
