"""
6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.
"""

nome_completo = input("Insira o seu nome completo: ")

nome = ""
i = 0
while True:
    if i == len(nome_completo):
        break
    if nome_completo[i] != " ":
        nome += nome_completo[i]
        i += 1
    else:
        break

sobrenome = ""
i = len(nome_completo) - 1
while True:
    if i == -1:
        break
    elif nome_completo[i] != " ":
        sobrenome = nome_completo[i] + sobrenome
        i -= 1
    else:
        break

print(f"Nome: {nome}\nSobrenome: {sobrenome}")