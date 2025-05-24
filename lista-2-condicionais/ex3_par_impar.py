"""
3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada.
"""

print("""
** PALPITES **
    Par = P
    Impar = I
""")

palpite_jogador_1 = input("Palpite do jogador 1 (P/I): ").upper()
palpite_jogador_2 = input("Palpite do jogador 2 (P/I): ").upper()

if (palpite_jogador_1 != "P" and palpite_jogador_1 != "I") or (palpite_jogador_2 != "P" and palpite_jogador_2 != "I"):
    print("Um ou ambos os jogadores inseriram um palpite inválido. Rodada não valeu!")
elif palpite_jogador_2 != palpite_jogador_1:
    num_jogador_1 = int(input("Número escolhido pelo jogador 1: "))
    num_jogador_2 = int(input("Número escolhido pelo jogador 2: "))

    if (1 <= num_jogador_1 <= 5) and (1 <= num_jogador_2 <= 5):
        soma = num_jogador_1 + num_jogador_2
        if soma % 2 == 0:
            resultado = "P"
            print("Resultado: PAR")
        else:
            resultado = "I"
            print("Resultado: IMPAR")

        if palpite_jogador_1 == resultado:
            print("O vencedor foi: Jogador 1!!")
        else:
            print("O vencedor foi: Jogador 2!!")
    else:
        print("Um ou ambos os jogadores inseriram um número inválido. Rodada não valeu!")
else:
    print("Jogador 2 escolheu o mesmo palpite que o jogar 1. Rodada não valeu!")