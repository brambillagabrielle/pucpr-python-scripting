# 7. Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
# de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
# Código de Exibição de Data
# • 1 – Data simples. Ex.: 10/08/1990;
# • 2 – Data abreviada. Ex.: 10/ago/1990;
# • 3 – Data completa. Ex.: 10 de agosto de 1990.

dia = int(input("Insira a dia (1-31): "))
mes = int(input("Insira o mês (1-12): "))
ano = int(input("Insira o ano (1000+): "))

if (1 <= dia <= 31) and (1 <= mes <= 12) and (1000 <= ano):
    print("""
    ** FORMATOS DE DATA **
        1 - Data simples. Ex.: 10/08/1990;
        2 - Data abreviada. Ex.: 10/ago/1990;
        3 - Data completa. Ex.: 10 de agosto de 1990.
    """)

    cod_exibicao = int(input("Insira um tipo de exibição de data para formatação: "))

    if mes == 2 and dia > 28:
        print("Dia não existe no mês 2. Data inserida é inválida!")
    elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
        print(f"Dia não existe no mês {mes} (maior do que 31). Data inserida é inválida!")
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
        print(f"Dia não existe no mês {mes} (maior do que 30). Data inserida é inválida!")
    else:
        if cod_exibicao == 1:
            print(f"Data formatada: {dia:02}/{mes:02}/{ano}")
        elif cod_exibicao == 2:
            if mes == 1:
                print(f"Data formatada: {dia:02}/jan/{ano}")
            elif mes == 2:
                print(f"Data formatada: {dia:02}/fev/{ano}")
            elif mes == 3:
                print(f"Data formatada: {dia:02}/mar/{ano}")
            elif mes == 4:
                print(f"Data formatada: {dia:02}/abr/{ano}")
            elif mes == 5:
                print(f"Data formatada: {dia:02}/mai/{ano}")
            elif mes == 6:
                print(f"Data formatada: {dia:02}/jun/{ano}")
            elif mes == 7:
                print(f"Data formatada: {dia:02}/jul/{ano}")
            elif mes == 8:
                print(f"Data formatada: {dia:02}/ago/{ano}")
            elif mes == 9:
                print(f"Data formatada: {dia:02}/set/{ano}")
            elif mes == 10:
                print(f"Data formatada: {dia:02}/out/{ano}")
            elif mes == 11:
                print(f"Data formatada: {dia:02}/nov/{ano}")
            else:
                print(f"Data formatada: {dia:02}/dez/{ano}")
        elif cod_exibicao == 3:
            if mes == 1:
                print(f"Data formatada: {dia:02} de janeiro de {ano}")
            elif mes == 2:
                print(f"Data formatada: {dia:02} de fevereiro de {ano}")
            elif mes == 3:
                print(f"Data formatada: {dia:02} de março de {ano}")
            elif mes == 4:
                print(f"Data formatada: {dia:02} de abril de {ano}")
            elif mes == 5:
                print(f"Data formatada: {dia:02} de maio de {ano}")
            elif mes == 6:
                print(f"Data formatada: {dia:02} de junho de {ano}")
            elif mes == 7:
                print(f"Data formatada: {dia:02} de julho de {ano}")
            elif mes == 8:
                print(f"Data formatada: {dia:02} de agosto de {ano}")
            elif mes == 9:
                print(f"Data formatada: {dia:02} de setembro de {ano}")
            elif mes == 10:
                print(f"Data formatada: {dia:02} de outubro de {ano}")
            elif mes == 11:
                print(f"Data formatada: {dia:02} de novembro de {ano}")
            else:
                print(f"Data formatada: {dia:02} de dezembro de {ano}")
        else:
            print("Código de formato de exibição inserido é inválido. Valide o valor informado!")
else:
    print("Dia, mês e/ou ano inserido(s) é(são) inválido(s). Valide a data informada!")