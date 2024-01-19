import random
import os


 
def imprimir_tabuleiro(tabuleiro):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in tabuleiro:
        print("|".join(row))

def verificar_vencedor(tabuleiro, vez):
    # Verificar se há um vencedor (horizontalmente)
    for row in tabuleiro:
        if vez * 4 in "".join(row):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {vez} venceu!")
            return True

    # Verificar se há um vencedor (verticalmente)
    for col in range(colunas):
        if vez * 4 in "".join([tabuleiro[row][col] for row in range(linhas)]):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {vez} venceu!")
            return True

    # Verificar se há um vencedor (diagonalmente)
    for i in range(linhas - 3):
        for j in range(colunas - 3):
            if tabuleiro[i][j] == tabuleiro[i + 1][j + 1] == tabuleiro[i + 2][j + 2] == tabuleiro[i + 3][j + 3] == vez:
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {vez} venceu!")
                return True
            elif tabuleiro[i][j + 3] == tabuleiro[i + 1][j + 2] == tabuleiro[i + 2][j + 1] == tabuleiro[i + 3][j] == vez:
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {vez} venceu!")
                return True

    return False

def jogar_quatro_em_linha():
    global linhas, colunas
    linhas = 8
    colunas = 8

    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]

    vez = "X"

    for _ in range(linhas * colunas):
        imprimir_tabuleiro(tabuleiro)

        if vez == "X":
            while True:
                try:
                    escolha = int(input(f"Jogador {vez}, escolha uma coluna (1-{colunas}): ")) - 1

                    if not (0 <= escolha < colunas):
                        raise ValueError("Escolha fora do intervalo permitido.")

                    for i in range(linhas - 1, -1, -1):
                        if tabuleiro[i][escolha] == " ":
                            tabuleiro[i][escolha] = vez
                            break
                    else:
                        print("Essa coluna está cheia. Escolha outra.")
                        continue

                    break  # Saia do loop se a escolha for válida

                except ValueError as e:
                    print(f"Erro: {e}")
                    continue
        else:
            # Computador faz escolhas aleatórias
            escolha = random.randint(0, colunas - 1)
            for i in range(linhas - 1, -1, -1):
                if tabuleiro[i][escolha] == " ":
                    tabuleiro[i][escolha] = vez
                    break

        if verificar_vencedor(tabuleiro, vez):
            return

        if vez == "X":
            vez = "O"
        else:
            vez = "X"

    imprimir_tabuleiro(tabuleiro)
    print("Empate!")

if __name__ == "__main__":
    jogar_quatro_em_linha()
