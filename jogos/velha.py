tabuleiro = [" "]*9

def desenhar_tabuleiro():
    print("---|---|---")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

def jogar_velha():
    jogador = "X"

    for _ in range(9):
        desenhar_tabuleiro()
        escolha = int(input("Jogador " + jogador + ", escolha uma posição (1-9): ")) - 1
        
        if tabuleiro[escolha] == " ":
            tabuleiro[escolha] = jogador
        else:
            print("Essa posição já está ocupada. Escolha outra.")
            continue
        
        # Verifica vitória
        if ((tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or #primeira linha
            (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or #segunda linha
            (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or #terceira linha
            (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or #vertical esquerda
            (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or #vertical do meio
            (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or#vertical da direita
            (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or#diagonal \
            (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador)): #diagonal /

            desenhar_tabuleiro()
            print("Jogador " + jogador + " venceu!")
            break

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

    else:
        desenhar_tabuleiro()
        print("Empate!")

if __name__ == "__main__":
    jogar_velha()