# velha.py

def desenhar_tabuleiro(tabuleiro):
    print("---|---|---")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

def limpar_tabuleiro():
    return [" "]*9

def verificar_vitoria(tabuleiro, jogador):
    # Verifica vitória
    return (
        (tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or
        (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or
        (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador) or
        (tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or
        (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or
        (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador) or
        (tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or
        (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador)
    )

def jogar_velha(jogador1, jogador2):
    pontos_jogador1 = 0
    pontos_jogador2 = 0

    while True:
        tabuleiro = limpar_tabuleiro()
        jogador = "X"
        
        while True:
            desenhar_tabuleiro(tabuleiro)

            try:
                escolha = int(input(f"{jogador}, escolha uma posição (1-9): ")) - 1

                if 0 <= escolha <= 8 and tabuleiro[escolha] == " ":
                    tabuleiro[escolha] = jogador
                else:
                    print("Posição inválida ou já ocupada. Escolha novamente.")
                    continue

            except ValueError:
                print("Entrada inválida. Digite um número de 1 a 9.")
                continue

            if verificar_vitoria(tabuleiro, jogador):
                desenhar_tabuleiro(tabuleiro)
                print(f"{jogador} venceu!")
                if jogador == "X":
                    pontos_jogador1 += 1
                else:
                    pontos_jogador2 += 1
                break

            if " " not in tabuleiro:
                desenhar_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador = "O" if jogador == "X" else "X"

        print(f"\nPontos de {jogador1}: {pontos_jogador1} pontos")
        print(f"Pontos de {jogador2}: {pontos_jogador2} pontos")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            break

if __name__ == "__main__":
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")

    jogar_velha(jogador1, jogador2)
