# 3. Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas
# 4 notas bimestrais. O algoritmo deve calcular a média destas notas, e uma
# mensagem informando que a média da disciplina nome é média.

nome_disciplina = input("Insira o nome da disciplina: ")

nota1 = float(input("Insira a nota do primeiro bimestre: "))
nota2 = float(input("Insira a nota do segundo bimestre: "))
nota3 = float(input("Insira a nota do terceiro bimestre: "))
nota4 = float(input("Insira a nota do quarto bimestre: "))

if nota1 > 0 and nota2 > 0 and nota3 > 0 and nota4 > 0:
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"A média da disciplina {nome_disciplina} é: {media}")
else:
    print("Uma ou mais notas inválidas. Média não pode ser calculada!")