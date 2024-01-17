def exibir_tabuleiro(tabuleiro):
    print("  0 1 2 3 4 5 6")
    for i, linha in enumerate(tabuleiro):
        print(chr(ord('A') + i), " ".join(linha))

def coordenada_para_indice(coordenada):
    coluna = ord(coordenada[0]) - ord('A')
    linha = int(coordenada[1])
    return linha, coluna

def indice_para_coordenada(indice):
    return f"{chr(ord('A') + indice[0])}{indice[1]}"

def verificar_moinho(tabuleiro, posicao, jogador):
    linha, coluna = posicao
    return (tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == tabuleiro[linha][3] == tabuleiro[linha][4] == tabuleiro[linha][5] == tabuleiro[linha][6] == jogador or
            tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] == tabuleiro[4][coluna] == tabuleiro[5][coluna] == tabuleiro[6][coluna] == jogador)

def verificar_movimento_valido(tabuleiro, inicio, fim):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    return 0 <= inicio[0] < linhas and 0 <= inicio[1] < colunas and 0 <= fim[0] < linhas and 0 <= fim[1] < colunas and tabuleiro[fim[0]][fim[1]] == '.' and (inicio[0] == fim[0] or inicio[1] == fim[1])

def fazer_movimento(tabuleiro, inicio, fim, jogador):
    tabuleiro[inicio[0]][inicio[1]] = '.'
    tabuleiro[fim[0]][fim[1]] = jogador

def main():
    # Inicializar o tabuleiro
    tabuleiro = [['.' for _ in range(7)] for _ in range(7)]

    # Loop principal do jogo
    jogador = 'X'
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador}")

        # Obter movimento do jogador atual
        inicio_coord = input("Informe as coordenadas de origem (por exemplo, A0): ")
        fim_coord = input("Informe as coordenadas de destino (por exemplo, B1): ")
        inicio = coordenada_para_indice(inicio_coord)
        fim = coordenada_para_indice(fim_coord)

        # Verificar se o movimento é válido
        if verificar_movimento_valido(tabuleiro, inicio, fim):
            fazer_movimento(tabuleiro, inicio, fim, jogador)
            if verificar_moinho(tabuleiro, fim, jogador):
                print(f"O jogador {jogador} formou um moinho!")
                peca_oponente = 'O' if jogador == 'X' else 'X'
                posicoes_moinho_oponente = [(i, j) for i in range(7) for j in range(7) if tabuleiro[i][j] == peca_oponente]
                if posicoes_moinho_oponente:
                    print(f"Remova uma peça do oponente:")
                    for idx, posicao in enumerate(posicoes_moinho_oponente):
                        print(f"{idx + 1}: {indice_para_coordenada(posicao)}")
                    indice_remover = int(input("Informe o número da peça a ser removida: ")) - 1
                    posicao_removida = posicoes_moinho_oponente[indice_remover]
                    tabuleiro[posicao_removida[0]][posicao_removida[1]] = '.'
            # Alternar para o outro jogador
            jogador = 'O' if jogador == 'X' else 'X'
        else:
            print("Movimento inválido. Tente novamente.")

if __name__ == "__main__":
    main()
