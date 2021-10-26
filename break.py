for n in range(1, 11):
    if n == 6:
        break
    else:
        print(n)

print('Saí do loop')


while True:
    if input('Digite "SAIR" para sair: ').upper() == 'SAIR':
        break