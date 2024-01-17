# velha.py

import json

tabuleiro = [" "]*9

def desenhar_tabuleiro():
    print("---|---|---")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

def limpar_tabuleiro():
    global tabuleiro
    tabuleiro = [" "]*9

def jogar_velha():
    global tabuleiro
    jogador = "X"
    
    while True:
        desenhar_tabuleiro()

        try:
            escolha = int(input("Jogador " + jogador + ", escolha uma posição (1-9): ")) - 1

            if 0 <= escolha <= 8 and tabuleiro[escolha] == " ":
                tabuleiro[escolha] = jogador
            else:
                print("Posição inválida ou já ocupada. Escolha novamente.")
                continue

        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 9.")
            continue

        # Verifica vitória
        if ((tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or
            (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or
            (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or
            (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or
            (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or
            (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or
            (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or
            (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador)):

            desenhar_tabuleiro()
            print("Jogador " + jogador + " venceu!")

            return jogador

        if " " not in tabuleiro:
            desenhar_tabuleiro()
            print("Empate!")

            return 0

        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"


if __name__ == "__main__":
    
    jogar_velha()
