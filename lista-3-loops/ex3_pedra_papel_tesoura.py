"""
3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
"""

while True:
    try:
        pontuacao_max = int(input("Insira a pontuação necessária para vencer o jogo: "))
    except:
        print(f"Erro encontrado na pontuação inserida! Tente novamente.")

    if pontuacao_max < 0:
        print("Pontuação inserida é menor ou igual a 0! Tente novamente.")
        continue
    break

pontuacao_jogador_1 = 0
pontuacao_jogador_2 = 0

while True:
    print("""
    ** OPÇÕES DE JOGADA **
        1 - Pedra
        2 - Papel
        3 - Tesoura
    """)

    try:
        jogador_1 = int(input("Insira a opção do Jogador 1: "))

        try:   
            jogador_2 = int(input("Insira a opção do Jogador 2: "))

            if (1 <= jogador_1 <= 3) and (1 <= jogador_2 <= 3):
                if jogador_1 == 1: # PEDRA
                    if jogador_2 == 1: # PEDRA
                        print("Empate!")
                    elif jogador_2 == 2: # PAPEL
                        print("Ponto para o Jogador 2!")
                        pontuacao_jogador_2 += 1
                    else: # TESOURA
                        print("Ponto para o Jogador 1!")
                        pontuacao_jogador_1 += 1
                elif jogador_1 == 2: # PAPEL
                    if jogador_2 == 1: # PEDRA
                        print("Ponto para o Jogador 1!")
                        pontuacao_jogador_1 += 1
                    elif jogador_2 == 2: # PAPEL
                        print("Empate!")
                    else: # TESOURA
                        print("Ponto para o Jogador 2!")
                        pontuacao_jogador_2 += 1
                else: # TESOURA
                    if jogador_2 == 1: # PEDRA
                        print("Ponto para o Jogador 2!")
                        pontuacao_jogador_2 += 1
                    elif jogador_2 == 2: # PAPEL
                        print("Ponto para o Jogador 1!")
                        pontuacao_jogador_1 += 1
                    else: # TESOURA
                        print("Empate!")

                if pontuacao_jogador_1 == pontuacao_max:
                    print(f"Jogador 1 venceu! Placar: {pontuacao_jogador_1} x {pontuacao_jogador_2}")
                    break
                elif pontuacao_jogador_2 == pontuacao_max:
                    print(f"Jogador 2 venceu! Placar: {pontuacao_jogador_1} x {pontuacao_jogador_2}")
                    break
            else:
                print("Um ou mais jogadores informaram uma opção inválida! Rodada não valeu!")
        except:
            print(f"Erro encontrado na opção inserida! Tente novamente.")
    except:
        print(f"Erro encontrado na opção inserida! Tente novamente.")