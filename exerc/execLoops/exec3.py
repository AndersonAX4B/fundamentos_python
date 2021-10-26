def verifica_nome():
    while True:
        nome = input('Digite o nome: ')
        if len(nome) >= 3:
            return nome
            break
        else:
            print('Nome menor do que 3 caracteres. Digite novamente', end=', ')


def verifica_idade():
    while True:
        try:
            idade = int(input('Digite a idade: '))
        except ValueError:
            print('Digite valor inteiro')
            continue

        if idade in range(1, 151):
            return idade
            break
        else:
            print('Digite apenas valores positivos e menor do 151')


def verifica_salario():
    while True:
        try:
            salario = float(input('Digite o salário: '))
        except ValueError:
            print('Digite apenas carateres numéricos')
            continue
        if salario >= 0:
            return salario
            break
        elif salario < 0:
            print('Digite apenas valores positivos')


def verifica_sexo():
    while True:
        sexo = input('Digite o sexo (F ou M): ')
        if sexo.upper() in ['F', 'M']:
            return sexo
            break
        else:
            print('Sexo não encontrado. Digite novamente', end=', ')


def verifica_estado_civil():
    while True:
        estado_civil = input('Digite o estado civil (S, C, V ou D): ')
        if estado_civil.upper() in ['S', 'C', 'V', 'D']:
            return estado_civil
            break
        else:
            print('Estado civil não encontrado. Digite novamente', end=', ')


user = {}

user = {'nome': verifica_nome(),
        'idade': verifica_idade(),
        'salario': verifica_salario(),
        'sexo': verifica_sexo(),
        'estado_civil': verifica_estado_civil()}

print(user)
