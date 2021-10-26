"""
Escrevendo um iterador customizado

Para criar um iterator é necessário declarar dois métodos mágicos, são eles: __iter__ e __next__

"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        raise StopIteration


con = Contador(1, 61)

it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print('\n')

for num in Contador(1, 8):
    print(num)

print('\n')
for num in range(1, 8):
    print(num)
