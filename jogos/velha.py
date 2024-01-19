import os

def imprimir_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")

def verificar_vitoria(tabuleiro, simbolo):
    linhas = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    colunas = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    diagonais = [[0, 4, 8], [2, 4, 6]]

    for linha in linhas + colunas + diagonais:
        if tabuleiro[linha[0]] == tabuleiro[linha[1]] == tabuleiro[linha[2]] == simbolo:
            return True
    return False

def jogo_velha(jogador1, jogador2):
    simbolos = ["X", "O"]
    jogadores = [jogador1, jogador2]
    vitorias = [0, 0]

    while True:
        pontuacao = [0, 0]
        partidas = 0 # Contador de partidas

        while partidas < 3: # Melhor de três
            tabuleiro = [" " for _ in range(9)]

            while True:
                for i in range(2):
                    imprimir_tabuleiro(tabuleiro)
                    print(f"\nTurno de {jogadores[i]} ({simbolos[i]})")
                    try: 

                        posicao = int(input("Escolha uma posição (1 a 9): ")) - 1
                    except:
                        print("Insira algo válido")

                    while tabuleiro[posicao] != " ":
                        print("Posição ocupada. Escolha outra.")
                        posicao = int(input("Escolha uma posição (1 a 9): ")) - 1

                    tabuleiro[posicao] = simbolos[i]

                    if verificar_vitoria(tabuleiro, simbolos[i]):
                        pontuacao[i] += 1
                        imprimir_tabuleiro(tabuleiro)
                        print(f"\n{jogadores[i]} ({simbolos[i]}) venceu!\n")
                        break

                    if " " not in tabuleiro:
                        imprimir_tabuleiro(tabuleiro)
                        print("\nEmpate!\n")
                        break

                if verificar_vitoria(tabuleiro, simbolos[0]) or verificar_vitoria(tabuleiro, simbolos[1]) or " " not in tabuleiro:
                    break

            partidas += 1 # Incrementa o contador de partidas

            imprimir_tabuleiro(tabuleiro) # Imprime o tabuleiro final da partida

            print(f"\n{jogadores[0]} está com {pontuacao[0]} pontos.")
            print(f"{jogadores[1]} está com {pontuacao[1]} pontos.")

            if (pontuacao[0] == 3 and pontuacao[1] == 0) or (pontuacao[0] == 2 and pontuacao[1] == 1): # Condição de vitória de uma melhor de três
                vitorias[0] += 1
                print(f"\n{jogadores[0]} está com {vitorias[0]} vitórias.")
                print(f"{jogadores[1]} está com {vitorias[1]} vitórias.")
                break

            if (pontuacao[0] == 0 and pontuacao[1] == 3) or (pontuacao[0] == 1 and pontuacao[1] == 2): # Condição de derrota de uma melhor de três
                vitorias[1] += 1
                print(f"\n{jogadores[0]} está com {vitorias[0]} vitórias.")
                print(f"{jogadores[1]} está com {vitorias[1]} vitórias.")
                break

            continuar = input("Deseja continuar? (s/n): ")
            if continuar.lower() != 's':
                break

        continuar = input("Deseja jogar novamente? (s/n): ")
        if continuar.lower() != 's':
            break

    relatorio = {
        "nomejogo": "velha",
        "jogador1": jogadores[0],
        "jogador2": jogadores[1],
        "vitoriasjg1": vitorias[0],
        "vitoriasjg2": vitorias[1],
        "pontosjg1": pontuacao[0],
        "pontosjg2": pontuacao[1]
    }

    return relatorio

if __name__ == "__main__":
    jg1 = input("Jogador 1: ")
    jg2 = input("Jogador 2: ")
    jogo_velha(jg1, jg2)
