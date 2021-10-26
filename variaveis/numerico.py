"""
Tipo Numérico


"""

num = 45

print(num)
print('\n')

# Somar
print(num + 4)
print('\n')

# Dividir
print(num / 4)

# Pegar um inteiro de uma divisão
print(int(num / 4))  # Usando Cast
print(num // 4)
print('\n')

# Multiplicar
print(num * 4)
print('\n')


# Saber o resto da divisão
print(num % 2)  # 0 é par e 1 é impar
print('\n')

# Elevar número
print(num ** 2)  # Não há limite para elevar um número, como há em outras linguagens, o limite é sua memória
print('\n')

# Facilitar o entendimento de uma valor em uma variável numérica
valor = 1_000_000_000
print(valor)

# Somar um valor simplificado
valor += 1
print(valor)

# Subtrair um valor simplificado
valor -= 1
print(valor)

# Dividir um valor simplificado
valor /= 1
print(valor)

# Multiplicar um valor simplificado
valor *= 1
print(valor)
print('\n')

# Dividir e retornar valor inteiro simplificado
num //= 4
print(num)
print('\n')

# Função de adiciona valor em uma variável numérica
add_valor = 10
print(add_valor.__add__(2))  # Não muda o valor padrão da variável
print(add_valor)
