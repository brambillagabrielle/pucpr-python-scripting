"""
9. Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas.
"""

try:
    num_decimal = int(input("Insira um número decimal: "))
except:
    print("Dígitos inseridos são inválidos!")
    exit(1)

if num_decimal < 1:
    print("Número hexadecimal não pôde ser calculado!")
    exit(1)

num_hexadecimal = ""
valor = num_decimal

while valor >= 1:
    div = int(valor / 16)
    resto = int(valor % 16)

    if resto == 10:
        num_hexadecimal = "A" + num_hexadecimal
    elif resto == 11:
        num_hexadecimal = "B" + num_hexadecimal
    elif resto == 12:
        num_hexadecimal = "C" + num_hexadecimal
    elif resto == 13:
        num_hexadecimal = "D" + num_hexadecimal
    elif resto == 14:
        num_hexadecimal = "E" + num_hexadecimal
    elif resto == 15:
        num_hexadecimal = "F" + num_hexadecimal
    else:
        num_hexadecimal = str(resto) + num_hexadecimal

    valor = div

print(f"Número hexadecimal = {num_hexadecimal}")