"""
5. Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B.
"""

pais_a = 5000000
pais_b = 7000000
quant_anos = 0

while True:
    if pais_a < pais_b:
        pais_a += pais_a * 0.03
        pais_b += pais_b * 0.02

        quant_anos += 1
    else:
        break

print(f"O País A passou o País B em população após {quant_anos} anos")