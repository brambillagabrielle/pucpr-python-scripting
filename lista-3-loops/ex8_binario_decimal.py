"""
8. Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal.
"""

num_binario = input("Insira um número binário: ")

num_decimal = 0

for i in range(len(num_binario)):
    try:
        ind = (len(num_binario) - 1) - i
        digito_binario = int(num_binario[ind])
    except:
        print("Caracteres inseridos são inválidos!")
        exit(1)

    if digito_binario == 0 or digito_binario == 1:
        num_decimal += digito_binario * 2**i
    else:
        print("Caracteres inseridos são dígitos inválidos para um número binário!")
        exit(1)

print(f"Número decimal = {num_decimal}")