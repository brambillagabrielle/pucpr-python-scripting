"""
1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos.
"""

while True:
    try:
        massa_inicial = float(input("Insira a massa inicial do material (gramas): "))
    except:
        print(f"Erro encontrado na leitura da massa do material! Tente novamente.")

    if massa_inicial <= 0:
        print("Massa inserida é menor ou igual a 0! Tente novamente.")
        continue

    break

print(f"Massa inicial inserida: {massa_inicial}g")

if massa_inicial < 0.5:
    print("Massa inserida já é menor que 0.5g - 0s")
    exit(0)

massa_final = massa_inicial
tempo_calc = 0

while massa_final > 0.5:
    massa_final /= 2
    tempo_calc += 50
    
print(f"Massa final: {massa_final}g - Tempo calculado: {tempo_calc}s")