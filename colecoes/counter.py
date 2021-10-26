"""
Módulo Collections - Counter

link docs Python -> https://docs.python.org/pt-br/3/library/collections.html

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento

"""

# Realizando o import do Counter
from collections import Counter

# Ex.1
# POdemos utilizar qualquer iterável
listas = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5]

# Utilizando o Counter
res = Counter(listas)

print(type(res))
print(res)
# Resposta: Counter({3: 11, 1: 3, 2: 3, 4: 3, 5: 2})
# Para cada elemento na lista, ele contou e retornou a quantidade de repetições de cada item na lista
print('\n')

# Ex.2
print(Counter('Anderson Peruci'))
# Counter({'n': 2, 'e': 2, 'r': 2, 'A': 1, 'd': 1, 's': 1, 'o': 1, ' ': 1, 'P': 1, 'u': 1, 'c': 1, 'i': 1})
print('\n')


# Ex.3
texto = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vitae blandit elit. In et risus suscipit, lacinia dolor in, scelerisque lectus. Nullam venenatis odio quis felis volutpat laoreet. Pellentesque ultrices pretium dui egestas euismod. Nulla sapien lacus, tincidunt ac tellus vitae, placerat convallis odio. Aenean lobortis tristique lacus eget molestie. Sed nunc nisl, dignissim at ligula nec, varius maximus sapien. Integer varius, mi eget commodo euismod, risus ligula semper sapien, eget laoreet nibh purus id urna. Aliquam erat volutpat. Integer nibh velit, tristique id interdum vel, semper ac lorem. Fusce hendrerit pretium sagittis. Nam sagittis pretium viverra. Aliquam erat volutpat. Sed ornare viverra justo, quis rutrum arcu placerat vitae.
Mauris feugiat varius neque non rhoncus. Praesent et cursus sem, euismod fermentum enim. Cras sed convallis lacus, a malesuada neque. Quisque neque felis, posuere et nulla at, cursus imperdiet lectus. Cras imperdiet risus nec elementum pretium. Ut consectetur cursus mattis. Ut vitae sodales tellus.
Nullam eleifend elementum massa, ac suscipit elit. Quisque vitae ante vitae orci tempus interdum eget non arcu. Pellentesque finibus odio et aliquam aliquam. Nullam tincidunt augue vel turpis posuere, et volutpat est finibus. Duis a velit est. Nunc in dolor auctor, aliquet eros id, ullamcorper lorem. Duis laoreet turpis vitae dictum pharetra. Nam in eros euismod, ultricies massa at, sollicitudin diam. In a sagittis magna. Fusce maximus, nisl imperdiet placerat fringilla, elit magna gravida mauris, ut interdum metus augue nec purus. Donec fringilla euismod tortor, et facilisis justo consequat non. Vivamus commodo consequat ipsum, ut sodales nunc consequat non. Integer vel elementum elit. Praesent viverra fermentum risus, sed tristique mi viverra id.
Proin elementum, nulla sed dignissim fringilla, sapien augue varius lacus, quis dignissim felis ante elementum odio. Nam ligula lacus, vestibulum id risus a, tristique vehicula lorem. Etiam elementum eget quam quis varius. Aliquam nisi turpis, volutpat ut ex sit amet, mattis molestie nunc. Suspendisse et orci in diam venenatis consectetur quis at sem. Sed in lectus quis lorem consequat convallis efficitur et ante. Morbi imperdiet, sapien vitae malesuada rhoncus, eros arcu eleifend leo, id molestie metus velit a lacus. Mauris varius commodo risus, ac faucibus sem interdum sed. Mauris finibus ante vehicula ullamcorper hendrerit. Vivamus mi lorem, faucibus eget eros eget, rhoncus cursus diam.
Pellentesque volutpat dolor at lacinia porta. Sed facilisis maximus arcu, a dignissim mauris. Praesent dolor metus, efficitur consequat mattis ac, eleifend vel metus. Quisque eros sapien, aliquet hendrerit nisi eget, gravida luctus arcu. Sed rutrum aliquam tempor. Proin id blandit ex. Proin posuere quam tortor, vitae consectetur turpis tempus eget. Donec sed tortor lobortis, tempus purus id, vulputate ipsum. Mauris ullamcorper erat ac nulla tincidunt dignissim. Quisque lectus ipsum, pharetra sed massa mollis, facilisis lacinia lorem. Etiam in felis efficitur, ullamcorper massa ac, fermentum purus. Ut venenatis eros sem, sit amet mattis mi finibus et. Donec risus felis, imperdiet quis euismod ut, tincidunt eget mi. """

palavras = texto.split()
# print(palavras)

# Ele conta quantas vezes uma palavra aparece no texto, ele identifica separado por espaço
count_palavra = Counter(palavras)
print(count_palavra)
# Counter({'et': 8, 'vitae': 7, 'quis': 7, 'eget': 7, 'eros': 6, 'dolor': 5, 'risus': 5, 'ac': 5, 'Sed': 5, 'id': 5, 'sed': 5, 'a': 5, 'elementum': 5, 'in': 5, 'consequat': 5, 'consectetur': 4, 'elit.': 4, 'Ut': 4, 'volutpat': 4, 'lacus,': 4, 'tincidunt': 4, 'tristique': 4, 'dignissim': 4, 'varius': 4, 'mi': 4, 'interdum': 4, 'lorem.': 4, 'Mauris': 4, 'cursus': 4, 'Quisque': 4, 'imperdiet': 4, 'ullamcorper': 4, 'sit': 3, 'lacinia': 3, 'Nullam': 3, 'venenatis': 3, 'felis': 3, 'Pellentesque': 3, 'pretium': 3, 'sapien': 3, 'placerat': 3, 'convallis': 3, 'at': 3, 'ligula': 3, 'Integer': 3, 'commodo': 3, 'Aliquam': 3, 'erat': 3, 'Nam': 3, 'viverra': 3, 'Praesent': 3, 'euismod': 3, 'fermentum': 3, 'nulla': 3, 'eleifend': 3, 'ante': 3, 'tempus': 3, 'finibus': 3, 'augue': 3, 'vel': 3, 'turpis': 3, 'massa': 3, 'ut': 3, 'Donec': 3, 'facilisis': 3, 'Proin': 3, 'mattis': 3, 'amet,': 2, 'blandit': 2, 'In': 2, 'lectus.': 2, 'odio': 2, 'odio.': 2, 'nunc': 2, 'maximus': 2, 'euismod,': 2, 'semper': 2, 'sapien,': 2, 'laoreet': 2, 'nibh': 2, 'purus': 2, 'volutpat.': 2, 'Fusce': 2, 'hendrerit': 2, 'sagittis': 2, 'rutrum': 2, 'arcu': 2, 'neque': 2, 'non': 2, 'sem,': 2, 'Cras': 2, 'malesuada': 2, 'felis,': 2, 'posuere': 2, 'at,': 2, 'nec': 2, 'sodales': 2, 'orci': 2, 'arcu.': 2, 'aliquam': 2, 'Duis': 2, 'velit': 2, 'aliquet': 2, 'id,': 2, 'diam.': 2, 'fringilla,': 2, 'gravida': 2, 'metus': 2, 'purus.': 2, 'tortor,': 2, 'non.': 2, 'Vivamus': 2, 'ipsum,': 2, 'risus,': 2, 'vehicula': 2, 'Etiam': 2, 'quam': 2, 'nisi': 2, 'molestie': 2, 'lectus': 2, 'efficitur': 2, 'faucibus': 2, 'eget,': 2, 'ac,': 2, 'Lorem': 1, 'ipsum': 1, 'adipiscing': 1, 'suscipit,': 1, 'in,': 1, 'scelerisque': 1, 'laoreet.': 1, 'ultrices': 1, 'dui': 1, 'egestas': 1, 'euismod.': 1, 'Nulla': 1, 'tellus': 1, 'vitae,': 1, 'Aenean': 1, 'lobortis': 1, 'lacus': 1, 'molestie.': 1, 'nisl,': 1, 'nec,': 1, 'sapien.': 1, 'varius,': 1, 'urna.': 1, 'velit,': 1, 'vel,': 1, 'sagittis.': 1, 'viverra.': 1, 'ornare': 1, 'justo,': 1, 'vitae.': 1, 'feugiat': 1, 'rhoncus.': 1, 'enim.': 1, 'neque.': 1, 'pretium.': 1, 'mattis.': 1, 'tellus.': 1, 'massa,': 1, 'suscipit': 1, 'aliquam.': 1, 'posuere,': 1, 'est': 1, 'finibus.': 1, 'est.': 1, 'Nunc': 1, 'auctor,': 1, 'dictum': 1, 'pharetra.': 1, 'ultricies': 1, 'sollicitudin': 1, 'magna.': 1, 'maximus,': 1, 'nisl': 1, 'elit': 1, 'magna': 1, 'mauris,': 1, 'fringilla': 1, 'justo': 1, 'id.': 1, 'elementum,': 1, 'vestibulum': 1, 'a,': 1, 'varius.': 1, 'turpis,': 1, 'ex': 1, 'nunc.': 1, 'Suspendisse': 1, 'diam': 1, 'sem.': 1, 'lorem': 1, 'ante.': 1, 'Morbi': 1, 'imperdiet,': 1, 'rhoncus,': 1, 'leo,': 1, 'lacus.': 1, 'sem': 1, 'sed.': 1, 'hendrerit.': 1, 'lorem,': 1, 'rhoncus': 1, 'porta.': 1, 'arcu,': 1, 'mauris.': 1, 'metus,': 1, 'metus.': 1, 'luctus': 1, 'tempor.': 1, 'ex.': 1, 'eget.': 1, 'tortor': 1, 'lobortis,': 1, 'vulputate': 1, 'ipsum.': 1, 'dignissim.': 1, 'pharetra': 1, 'mollis,': 1, 'efficitur,': 1, 'amet': 1, 'et.': 1, 'ut,': 1, 'mi.': 1})
print('\n')

# Pegar o itens mais comuns
print(count_palavra.most_common(3))  # Quantidade de itens que serão retornados
# print(help(Counter))
