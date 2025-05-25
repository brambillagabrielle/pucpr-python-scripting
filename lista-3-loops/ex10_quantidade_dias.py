"""
10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos).
"""

dia_1 = int(input("Insira a dia (1-31) da data 1: "))
mes_1 = int(input("Insira o mês (1-12) da data 1: "))
ano_1 = int(input("Insira o ano (1000+) da data 1: "))

dia_2 = int(input("Insira a dia (1-31) da data 2: "))
mes_2 = int(input("Insira o mês (1-12) da data 2: "))
ano_2 = int(input("Insira o ano (1000+) da data 2: "))

cont_dias = 0

if ano_1 < ano_2:
    maior_data = 1
    dia = dia_1
    mes = mes_1
    ano = ano_1
elif ano_2 < ano_1:
    maior_data = 2
    dia = dia_2
    mes = mes_2
    ano = ano_2
else:
    if mes_1 < mes_2:
        maior_data = 1
        dia = dia_1
        mes = mes_1
        ano = ano_1
    elif mes_2 < mes_1:
        maior_data = 2
        dia = dia_2
        mes = mes_2
        ano = ano_2
    else:
        if dia_1 < dia_2:
            maior_data = 1
            dia = dia_1
            mes = mes_1
            ano = ano_1
        elif dia_2 < dia_1:
            maior_data = 2
            dia = dia_2
            mes = mes_2
            ano = ano_2
        else:
            maior_data = 0

while True:
    if maior_data == 0:
        break
    elif maior_data == 1 and ((dia != dia_2) or (mes != mes_2) or (ano != ano_2)):
        cont_dias += 1
    elif maior_data == 2 and ((dia != dia_1) or (mes != mes_1) or (ano != ano_1)):
        cont_dias += 1
    else:
        break

    dia += 1

    if mes == 2:
        if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0 and dia >= 30:
            dia = 1
            mes += 1
        elif dia >= 29:
            dia = 1
            mes += 1
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10) and dia >= 32:
        dia = 1
        mes += 1
    elif (mes == 12) and (dia >= 32):
        dia = 1
        mes = 1
        ano += 1
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia >= 31:
        dia = 1
        mes += 1

print(f"Contagem de dias: {cont_dias}")