# 2. Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula
# sua idade com relação ao ano de 2020, sendo que o usuário já fez aniversário
# neste ano.

ano_nascimento = int(input("Insira o ano do seu nascimento: "))
ano_referencia = 2020

if 1900 < ano_nascimento < ano_referencia:
    idade = ano_referencia - ano_nascimento
    print(f"Idade calculada: {idade}")
else:
    print("Ano inserido é inválido!")