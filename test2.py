# print(chr(1))
#
# print(ord("?"))
#
# print(hex(14389754378953498))
#
# print(oct(14389754378953498))

# print(x[::-1])
# x = [1,2,3,4,5]

# x = bool(-3)
# y = bool("True"*x)
# z = bool("False")
#
# print(x and y and z)

# from datetime import date

# dates = [date(2014, 3, 2), date(2043, 8, 1), date(2023, 9, 5), date(2098, 12, 30)]
# print(type(max([dates])))

"""context = None
if not context:
    print(1)
"""

# print("Olá João Futi".replace("Ola", "Oi"))

lista = [1, 2, 3, 4]
lista[2] = 6

print(lista)

tupla = (1, 2, 3, 4)

print(tupla)

dicionario = {}
print(dicionario)

for index, value in enumerate(lista):
    dicionario.update({index: value})

print(dicionario)

dicionario2 = {True: 1, True: 3, False: 8, False: 9}
print(dicionario2)
