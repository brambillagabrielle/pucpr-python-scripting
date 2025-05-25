"""
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
"""

numeros = []

i = 0
while len(numeros) < 5:    
    try:
        num = int(input(f"Insira o {i + 1}º número: "))
        
        i += 1

        if numeros == []:
            numeros = [num]
            continue

        for j in range(len(numeros)):
            if num < numeros[j]:
                numeros.insert(j, num)
                break
            elif j == (len(numeros) - 1):
                numeros += [num]
    except:
        print("Valor inserido é inválido, tente novamente!")

print(f"Números inseridos: {numeros}")