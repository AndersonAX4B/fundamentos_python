"""
Decoradores (Decorators)

O que são decorators
 - Decorators são funções;
 - Decorators envolvem outras funções e aprimoram seus comportamentos
 - Decorators também são exemplos de Higher Order Functions;
    - Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)
|----------------------------------------|
|      Function Decorator                |
|----------------------------------------|

|-------------------------------------------|
| |---------------------------------------| |
| |        Função decorada                | |
| |---------------------------------------| |
|-------------------------------------------|


"""


# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)
# Não recomendado decorar do jeito abaixo
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')

    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')


# Testando 1
teste = seja_educado(saudacao)
teste()
print('\n')


# Decorators com syntax Sugar - MANEIRA RECOMENDADA
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')

    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando
apresentando()
print('\n')
