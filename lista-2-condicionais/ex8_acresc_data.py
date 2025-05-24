"""
8. Implemente um programa que solicite uma data com hora, pedindo em separado: dia,
mês, ano, hora, minuto e segundo. Pergunte ao usuário que informação ele deseja
acrescentar, e em qual quantidade. Informar a nova data de acordo com o solicitado pelo
usuário.
Para determinar se um ano é bissexto, execute estas etapas:
 1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá
para a etapa 5.
 2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário,
vá para a etapa 4.
 3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário,
vá para a etapa 5.
 4. O ano é bissexto (tem 366 dias).
 5. O ano não é um ano bissexto (tem 365 dias).
"""
 
dia = int(input("Insira a dia (1-31): "))
mes = int(input("Insira o mês (1-12): "))
ano = int(input("Insira o ano (1000+): "))
hora = int(input("Insira a dia (0-23): "))
minuto = int(input("Insira a dia (0-59): "))
segundo = int(input("Insira a dia (0-59): "))

if (1 <= dia <= 31) and (1 <= mes <= 12) and (1000 <= ano) and (0 <= hora <= 23)and (0 <= minuto <= 59)and (0 <= segundo <= 59):
    print(f"Data inserida: {dia}/{mes}/{ano}-{hora}:{minuto}:{segundo}")
    
    print(f"""
    ** INFORMAÇÕES **
        1 - Segundo = {segundo} + x segundo(s)
        2 - Minuto = {minuto} + x minuto(s)
        3 - Hora = {hora} + x hora(s)
        4 - Dia = {dia} + x dia(s)
        5 - Mês = {mes} + x mes(es)
        6 - Ano = {ano} + x ano(s)
    """)
    
    cod_informacao = int(input("O que deseja acrescentar? (1-6): "))
    quantidade = int(input("Insira a quantidade para acrescentar (ex: 4 para +4 dias): "))

    if quantidade > 0:
        if cod_informacao == 1:
            segundo_acresc = segundo + quantidade

            if segundo_acresc > 60:
                quantidade = segundo_acresc / 60
                segundo = segundo_acresc % 60

                minuto_acresc = minuto + quantidade
                if minuto_acresc > 60:
                    quantidade = minuto_acresc / 60
                    minuto = minuto_acresc % 60

                    hora_acresc = hora + quantidade
                    if hora_acresc > 24:
                        quantidade = hora_acresc / 24
                        hora = hora_acresc % 24

                        dia_acresc = dia + quantidade
                        if dia_acresc > 30:
                            quantidade = dia_acresc / 30
                            dia = dia_acresc % 30

                            mes_acresc = mes + quantidade
                            if mes_acresc > 12:
                                quantidade = mes_acresc / 12
                                mes = mes_acresc % 12

                                ano += quantidade
                            else:
                                mes = mes_acresc
                        else:
                            dia = dia_acresc
                    else:
                        hora = hora_acresc
                else:
                    minuto = minuto_acresc
            else:
                segundo = segundo_acresc
        elif cod_informacao == 2:
            minuto_acresc = minuto + quantidade
            if minuto_acresc > 60:
                quantidade = minuto_acresc / 60
                minuto = minuto_acresc % 60

                hora_acresc = hora + quantidade
                if hora_acresc > 24:
                    quantidade = hora_acresc / 24
                    hora = hora_acresc % 24

                    dia_acresc = dia + quantidade
                    if dia_acresc > 30:
                        quantidade = dia_acresc / 30
                        dia = dia_acresc % 30

                        mes_acresc = mes + quantidade
                        if mes_acresc > 12:
                            quantidade = mes_acresc / 12
                            mes = mes_acresc % 12

                            ano += quantidade
                        else:
                            mes = mes_acresc
                    else:
                        dia = dia_acresc
                else:
                    hora = hora_acresc
            else:
                minuto = minuto_acresc
        elif cod_informacao == 3:
            hora_acresc = hora + quantidade
            if hora_acresc > 24:
                quantidade = hora_acresc / 24
                hora = hora_acresc % 24

                dia_acresc = dia + quantidade
                if dia_acresc > 30:
                    quantidade = dia_acresc / 30
                    dia = dia_acresc % 30

                    mes_acresc = mes + quantidade
                    if mes_acresc > 12:
                        quantidade = mes_acresc / 12
                        mes = mes_acresc % 12

                        ano += quantidade
                    else:
                        mes = mes_acresc
                else:
                    dia = dia_acresc
            else:
                hora = hora_acresc
        elif cod_informacao == 4:
            dia_acresc = dia + quantidade
            if dia_acresc > 30:
                quantidade = dia_acresc / 30
                dia = dia_acresc % 30

                mes_acresc = mes + quantidade
                if mes_acresc > 12:
                    quantidade = mes_acresc / 12
                    mes = mes_acresc % 12

                    ano += quantidade
                else:
                    mes = mes_acresc
            else:
                dia = dia_acresc
        elif cod_informacao == 5:
            mes_acresc = mes + quantidade
            if mes_acresc > 12:
                quantidade = mes_acresc / 12
                mes = mes_acresc % 12

                ano += quantidade
            else:
                mes = mes_acresc
        elif cod_informacao == 6:
            ano += quantidade
        else:
            print("Código informado é inválido!")
            exit(1)

        print(f"Data atualizada: {round(dia)}/{round(mes)}/{round(ano)}-{round(hora)}:{round(minuto)}:{segundo}")
    else:
        print("Quantidade informada é inválida!")
else:
    print("Dia, mês, ano, hora, minuto e/ou segundos inserido(s) é(são) inválido(s). Valide as informações enviadas!")