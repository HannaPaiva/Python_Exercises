
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

def jogo_velha():
    simbolos = ["X", "O"]
    jogadores = [input("Nome do jogador 1: "), input("Nome do jogador 2: ")]
    pontuacao = [0, 0]
    vitorias = [0, 0]

    while True: # Loop principal do jogo
        tabuleiro = [" " for _ in range(9)]
        partidas_vencidas = [0, 0]

        while True: # Loop de uma melhor de três
            for i in range(2): # Loop de um turno
                imprimir_tabuleiro(tabuleiro)
                print(f"\nTurno de {jogadores[i]} ({simbolos[i]})")
                try:
                 posicao = int(input("Escolha uma posição (1 a 9): ")) - 1
                except:
                    print("Insira uma entrada válida")
                while tabuleiro[posicao] != " ":
                    print("Posição ocupada ou inválida. Escolha outra.")
                    try:
                        posicao = int(input("Escolha uma posição (1 a 9): ")) - 1
                    except:
                        print("Posição ocupada ou inválida. Escolha outra.")

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
                partidas_vencidas[0 if vitorias[0] > vitorias[1] else 1] += 1

                print(f"\n{jogadores[0]} está com {pontuacao[0]} pontos.")
                print(f"{jogadores[1]} está com {pontuacao[1]} pontos.")
            

                continuar = input("Deseja continuar? (s/n): ")
                if continuar.lower() != 's':
                    break 
                    
                else:
                    tabuleiro = [" " for _ in range(9)]
                

        if partidas_vencidas[0] == 2 or partidas_vencidas[1] == 2:
            vitorias[0] += 1 # Adiciona um ponto de vitória ao vencedor da melhor de três
            vitorias[1] += 0 # Não adiciona nenhum ponto de vitória ao perdedor da melhor de três
            print(f"\n{jogadores[0]} está com {vitorias[0]} vitórias.")
            print(f"{jogadores[1]} está com {vitorias[1]} vitórias.")
            break

        continuar = input("Deseja jogar novamente? (s/n): ")
        if continuar.lower() == 'n':
            if partidas_vencidas[0] == 2 or partidas_vencidas[1] == 2:
                vitorias[0] += partidas_vencidas[0]
                vitorias[1] += partidas_vencidas[1]
                break
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
    jogo_velha()
