"""
4. Elaborar um algoritmo que solicita o nome de um produto, seu valor e
quantidade, informando o valor de compra calculado.
"""

nome_produto = input("Insira o nome do produto: ")
valor_produto = float(input("Insira o valor do produto: "))
quantidade_produto = int(input("Insira a quantidade do produto: "))

if valor_produto > 0 and quantidade_produto > 0:
    valor_calculado = valor_produto * quantidade_produto
    print(f"Valor de compra calculado: R$ {valor_calculado:.2f}")
else:
    print("Valor do produto ou quantidade inserida inválida")