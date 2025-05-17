# 2. O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
# para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
# = peso / altura2. Implemente um programa que leia o peso e a altura de um adulto e mostre
# sua condição de acordo com a tabela abaixo.
# IMC em adultos Condição
# • Abaixo de 18,5 – Abaixo do peso
# • Entre 18,5 e 25 – Peso normal
# • Entre 25 e 30 – Acima do peso
# • Acima de 30 – Obeso

peso = float(input("Informe o seu peso (0+): "))
altura = float(input("Informe a sua altura (0+): "))

if peso <= 0 or altura <= 0:
    print("Altura e/ou peso inválidos")
else:
    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Resultado: Abaixo do peso")
    elif imc < 25:
        print("Resultado: Peso normal")
    elif imc < 30:
        print("Resultado: Acima do peso")
    else:
        print("Resultado: Obeso")