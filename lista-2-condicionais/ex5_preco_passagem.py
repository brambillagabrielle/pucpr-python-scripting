"""
5. Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno
(ida e volta) e informar o preço da passagem conforme a tabela a seguir:
 Condição              Ida         Ida e volta
 Região Norte          R$ 500,00   R$ 900,00
 Região Nordeste       R$ 350,00   R$ 650,00
 Região Centro-Oeste   R$ 350,00   R$ 600,00
 Região Sul            R$ 300,00   R$ 550,00
"""
 
print("""
** REGIÕES DE DESTINO **
    Norte = NO
    Nordeste = NE
    Centro-Oeste = CE
    Sul = SU
""")

destino = input("Insira a região de destino do passageiro (NO/NE/CE/SU): ").upper()

if destino == "NO" or destino == "NE" or destino == "CE" or destino == "SU":
    passagemIda = input("Passagem só de ida? (S/N): ").upper()

    if passagemIda == "S":
        if destino == "NO":
            print(f"Valor da passagem só de ida para {destino}: R$ {500.00:.2f}")
        elif destino == "NE" or destino == "C0":
            print(f"Valor da passagem só de ida para {destino}: R$ {350.00:.2f}")
        else:
            print(f"Valor da passagem só de ida para {destino}: R$ {300.00:.2f}")
    elif passagemIda == "N":
        if destino == "NO":
            print(f"Valor da passagem só de ida para {destino}: R$ {900.00:.2f}")
        if destino == "NE":
            print(f"Valor da passagem só de ida para {destino}: R$ {650.00:.2f}")
        if destino == "CO":
            print(f"Valor da passagem só de ida para {destino}: R$ {600.00:.2f}")
        else:
            print(f"Valor da passagem só de ida para {destino}: R$ {550.00:.2f}")
    else:
        print("Confirmação da quantidade de passagens é inválida!")
else:
    print("Região de destino inserida é inválida!")