"""
1. Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
 • para homens: (72.7 * h) – 58;
 • para mulheres: (62.1 * h) – 44.7.
"""

altura = float(input("Informe a sua altura (0+): "))

# .upper() = transforma string para caracteres maiúsculos
sexo = input("Informe o seu sexo (F/M): ").upper()

if altura > 0.0:
    # if sexo == "F" or sexo == "f":
    if sexo == "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Peso ideal (Mulheres): {peso_ideal:.2f} kg")
    elif sexo == "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"Peso ideal (Homens): {peso_ideal:.2f} kg")
    else:
        print("Sexo informado é inválido!")
else:
    print("Altura informada é inválida!")