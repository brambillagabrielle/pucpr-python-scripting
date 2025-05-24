"""
5. Estender o exercício 4 anterior informando que para pagamento à vista tem
15% de desconto, calculando e exibindo este valor.
"""

nome_produto = input("Insira o nome do produto: ")
valor_produto = float(input("Insira o valor do produto: "))
quantidade_produto = int(input("Insira a quantidade do produto: "))

if valor_produto > 0 and quantidade_produto > 0:
    valor_calculado = valor_produto * quantidade_produto
    desconto = valor_calculado * 0.15
    valor_total = valor_calculado - desconto
    
    print(f"Valor de compra calculado: R$ {valor_calculado:.2f}")
    print("Para pagamento à vista, temos 15% de desconto: ",
          f"R$ {valor_total:.2f} (-R$ {desconto:.2f})")
else:
    print("Valor do produto ou quantidade inserida inválida")