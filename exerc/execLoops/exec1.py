while True:
    nota = int(input('Digite um valor entre 0 e 10: '))
    if nota in range(0, 11):
        break
    else:
        print('Valor inválido')

