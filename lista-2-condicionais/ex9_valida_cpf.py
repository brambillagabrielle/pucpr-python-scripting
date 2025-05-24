"""
9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada
um dos 11 dígitos do CPF.
Definição:
O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##", a
verificação do CPF acontece utilizando os 9 primeiros dígitos e, com um cálculo simples,
verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
Vamos usar como exemplo, um CPF fictício "529.982.247-25".
Validação do primeiro dígito
Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de
números de 10 à 2 e soma os resultados. Assim:
5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2
O resultado do nosso exemplo é: 295
O próximo passo da verificação também é simples, basta multiplicarmos esse resultado
por 10 e dividirmos por 11.
295 * 10 / 11
O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual
ao primeiro dígito verificador (primeiro dígito depois do '-'), a primeira parte da
validação está correta.
Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como 0.
O resultado da divisão acima é '268' e o RESTO é 2
Isso significa que o nosso CPF exemplo passou na validação do primeiro dígito.
Validação do segundo dígito
A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9
primeiros dígitos, mais o primeiro dígito verificador, e vamos multiplicar esses 10
números pela sequencia decrescente de 11 a 2. Vejamos:
5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2
O resultado é: 347
Seguindo o mesmo processo da primeira verificação, multiplicamos por 10 e dividimos
por 11.
347 * 10 / 11
Verificando o RESTO, como fizemos anteriormente, temos:
O resultado da divisão é '315' e o RESTO é 5
Verificamos, se o resto corresponde ao segundo dígito verificador.
Com essa verificação, constatamos que o CPF 529.982.247-25 é válido.
"""

digito_1 = int(input("Insira o 1º dígito do CPF: "))
digito_2 = int(input("Insira o 2º dígito do CPF: "))
digito_3 = int(input("Insira o 3º dígito do CPF: "))
digito_4 = int(input("Insira o 4º dígito do CPF: "))
digito_5 = int(input("Insira o 5º dígito do CPF: "))
digito_6 = int(input("Insira o 6º dígito do CPF: "))
digito_7 = int(input("Insira o 7º dígito do CPF: "))
digito_8 = int(input("Insira o 8º dígito do CPF: "))
digito_9 = int(input("Insira o 9º dígito do CPF: "))
digito_10 = int(input("Insira o 10º dígito do CPF: "))
digito_11 = int(input("Insira o 11º dígito do CPF: "))

print(f"CPF inserido: {digito_1}{digito_2}{digito_3}.{digito_4}{digito_5}{digito_6}.{digito_7}{digito_8}{digito_9}-{digito_10}{digito_11}")

soma_verif_1 = (digito_1 * 10) + (digito_2 * 9) + (digito_3 * 8) + (digito_4 * 7) + (digito_5 * 6) + (digito_6 * 5) + (digito_7 * 4) + (digito_8 * 3) + (digito_9 * 2)
resto_verif_1 = (soma_verif_1 * 10) % 11

if resto_verif_1 == 10:
    resto_verif_1 = 0

cpf_correto = True

if resto_verif_1 == digito_10:
    print("O dígito verificador 1 é está correto!")
else:
    print("O dígito verificador 1 NÃO está correto!")
    cpf_correto = False

soma_verif_2 = (digito_1 * 11) + (digito_2 * 10) + (digito_3 * 9) + (digito_4 * 8) + (digito_5 * 7) + (digito_6 * 6) + (digito_7 * 5) + (digito_8 * 4) + (digito_9 * 3) + (digito_10 * 2)
resto_verif_2 = (soma_verif_2 * 10) % 11

if resto_verif_2 == 10:
    resto_verif_2 = 0

if resto_verif_2 == digito_11:
    print("O dígito verificador 2 é está correto!")
else:
    print("O dígito verificador 2 NÃO está correto!")
    cpf_correto = False

if cpf_correto:
    print("CPF validado com sucesso!")
else:
    print("CPF inválido. Verificar os dígitos inseridos!")