# 4. Implemente um programa que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
# os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
# cálculo adequado.
# Código Condição de pagamento
# • 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
# • 2 – À vista no cartão de crédito, recebe 15% de desconto
# • 3 – Em duas vezes, preço normal de etiqueta sem juros
# • 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%

print("""
** CONDICOES DE PAGAMENTO **
    1 - À vista em dinheiro ou cheque, recebe 10% de desconto
    2 - À vista no cartão de crédito, recebe 15% de desconto
    3 - Em duas vezes, preço normal de etiqueta sem juros
    4 - Em duas vezes, preço normal de etiqueta mais juros de 10%
""")

valor_produto = float(input("Insira o preço normal de etiqueta do produto (1+): "))
cond_pagamento = int(input("Insira a condição de pagamento (1-4): "))

if cond_pagamento == 1:
    valor_total = valor_produto - (valor_produto * 0.10)
    print(f"À vista em dinheiro ou cheque, o valor total a pagar é de: R$ {valor_total:.2f}")
elif cond_pagamento == 2:
    valor_total = valor_produto - (valor_produto * 0.15)
    print(f"À vista no cartão de crédito, o valor total a pagar é de: R$ {valor_total:.2f}")
elif cond_pagamento == 3:
    prestacao = valor_produto / 2
    print(f"Em duas vezes, o valor de cada prestação é de: R$ {prestacao:.2f} (sem juros)")
elif cond_pagamento == 4:
    prestacao = valor_produto / 2
    prestacao += prestacao * 0.15
    print(f"Em duas vezes, o valor de cada prestação é de: R$ {prestacao:.2f} (com 15% de juros)")
else:
    print("Preço do produto ou condição de pagamento são inválidos!")