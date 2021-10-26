"""
Filter

filter() -> serve para filtrar dados em determinada coleção


"""
# Lib para trabalhar com dados estatísticos
from statistics import mean

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Obs.: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável
# Funcionamento: a condição no filter(dado > mean(dados)) retornará verdadeiro ou falso, é com base nisso
# que o filter saberá se ele armazerá o valor ou não
res = filter(lambda dado: dado > 1, dados)
print(type(res))  # Retorna o tipo Filter Object, é iterável e convertível
print(list(res))
# Assim como o map, o valor também é deletado da memória após ser usado pela primeira vez
print(list(res))
print('\n')

# Exemplo
# Filter é muito usado em ciência de dados, para remover dados faltantes

paises = ['', 'Brasil', '', '', '', 'Argentina', 'Chile', '', 'México']

# Filter para limpar vazios
# remove_vazio = filter(lambda pais: len(pais) > 0, paises)  # Outra solução para limpar - Lambda
# remove_vazio = filter(lambda pais: pais != '' ,paises)
remove_vazio = filter(None, paises)
print(list(remove_vazio))
print('\n')

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e uma iterável e
#   retorna um objeto mapeando a função para cada elemento do iterável.
#   A função que é passada ao map() retorna valores


# filter() -> Recebe dois parâmetros, uma função e um iterável e
#   retorna um objeto filtrando apenas os elementos de acordo com a função
#   A função que é passada ao filter() retorna valores True ou False, é assim que o dado é ou não armazenado


# Exemplo mais complexo
usuarios = [
    {"username": "samuel", "tweets": ["Eu adodo bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
# Filtrar os usuários que estão inativos no Twitter
# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutrura é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
