# 6. Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
# os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
# raízes devem ser calculadas pela fórmula de Bhaskara,

a = int(input("Insira o valor do coeficiente a = "))
b = int(input("Insira o valor do coeficiente b = "))
c = int(input("Insira o valor do coeficiente c = "))

if a != 0:
    delta = b**2 - (4 * a * c)
    print(delta)

    if delta < 0:
        print("Resultado: Equação não possui resultados reais")
    else:
        x1 = (-b + delta**(1/2)) / (2 * a)

        if delta > 0:
            x2 = (-b + (-delta**(1/2))) / (2 * a)
            print(f"Resultados: x1 = {x1} | x2 = {x2}")
        else:
            print(f"Resultados: x1 = {x1} | x2 = {x1}")
else:
    print("Coeficiente a não pode ser igual à 0!")