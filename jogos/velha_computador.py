import random

tabuleiro = [" "]*9

def desenhar_tabuleiro():
    print("---|---|---")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

def jogada_jogador(jogador):
    escolha = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
    if tabuleiro[escolha] == " ":
        tabuleiro[escolha] = jogador
        return True
    else:
        print("Essa posição já está ocupada. Escolha outra.")
        return False

def jogada_computador():
    escolhas_disponiveis = [i for i in range(9) if tabuleiro[i] == " "]
    if escolhas_disponiveis:
        escolha = random.choice(escolhas_disponiveis)
        tabuleiro[escolha] = "O"
        return True
    return False

def jogar_velha():
    global tabuleiro
    tabuleiro = [" "]*9
    jogador_em_numeros = 0  # 0 representa empate, 1 para jogador X, 2 para jogador O
    jogador_atual = "X"

    for _ in range(9):
        desenhar_tabuleiro()

        if jogador_atual == "X":
            jogada_valida = jogada_jogador(jogador_atual)
        else:
            print("\nVez do Computador (O):")
            jogada_valida = jogada_computador()

        if jogada_valida:
            # Verifica vitória
            if ((tabuleiro[0] == jogador_atual and tabuleiro[1] == jogador_atual and tabuleiro[2] == jogador_atual) or
                (tabuleiro[3] == jogador_atual and tabuleiro[4] == jogador_atual and tabuleiro[5] == jogador_atual) or
                (tabuleiro[6] == jogador_atual and tabuleiro[7] == jogador_atual and tabuleiro[8] == jogador_atual) or
                (tabuleiro[0] == jogador_atual and tabuleiro[3] == jogador_atual and tabuleiro[6] == jogador_atual) or
                (tabuleiro[1] == jogador_atual and tabuleiro[4] == jogador_atual and tabuleiro[7] == jogador_atual) or
                (tabuleiro[2] == jogador_atual and tabuleiro[5] == jogador_atual and tabuleiro[8] == jogador_atual) or
                (tabuleiro[0] == jogador_atual and tabuleiro[4] == jogador_atual and tabuleiro[8] == jogador_atual) or
                (tabuleiro[2] == jogador_atual and tabuleiro[4] == jogador_atual and tabuleiro[6] == jogador_atual)):

                desenhar_tabuleiro()
                print(f"Jogador {jogador_atual} venceu!")
                jogador_em_numeros = 1 if jogador_atual == "X" else 2
                return jogador_em_numeros

            jogador_atual = "O" if jogador_atual == "X" else "X"

    else:
        desenhar_tabuleiro()
        print("Empate!")
        return jogador_em_numeros

if __name__ == "__main__":
    jogar_velha()
