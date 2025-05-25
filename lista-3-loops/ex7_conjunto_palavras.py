"""
7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras.
"""

palavras = []
while True:
    palavra = input("Digite uma palavra (ou saia apertando ENTER): ")

    if palavra != "":
        palavras += [palavra]
    else:
        break

print(f"Palavras informadas: {palavras}")

contagem = 0
for i in range(len(palavras)):
    for j in range(len(palavras[i])):
        if palavras[i][j].upper() == "A":
            contagem += 1
            print(palavras[i][j])

print(f"Quantidade de letras A encontradas: {contagem}")