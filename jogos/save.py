import random

def criar_tabuleiro(linhas, colunas, num_navios):
    if linhas * colunas < num_navios:
        print("Número de navios é maior que o tamanho do tabuleiro.")
        return None

    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    posicoes_navios = []

    for _ in range(num_navios):
        orientacao = random.choice(['horizontal', 'vertical'])
        tamanho_navio = random.randint(2, min(linhas, colunas))  # Tamanho do navio limitado pelo tamanho menor

        if orientacao == 'horizontal':
            x = random.randint(0, colunas - tamanho_navio)
            y = random.randint(0, linhas - 1)
            for i in range(tamanho_navio):
                tabuleiro[y][x + i] = i + 1  # Marcando as posições do navio
                posicoes_navios.append((y, x + i))
        else:
            x = random.randint(0, colunas - 1)
            y = random.randint(0, linhas - tamanho_navio)
            for i in range(tamanho_navio):
                tabuleiro[y + i][x] = i + 1  # Marcando as posições do navio
                posicoes_navios.append((y + i, x))

    return tabuleiro, posicoes_navios

def imprimir_tabuleiro(tabuleiro, revelado):
    cabecalho = "  " + " ".join(chr(65 + col) for col in range(len(tabuleiro[0])))  # LETRAS/COLUNAS
    print(cabecalho)

    for linha, dados_linha in enumerate(tabuleiro):  # cada linha da matriz // valor + índice
        linha_str = f"{linha} "

        for coluna, dados_coluna in enumerate(dados_linha):  # cada coluna
            if revelado[linha][coluna]:
                linha_str += str(dados_coluna) + " "  # ESCOLHIDO --> REVELAR
            else:
                linha_str += ". "

        print(linha_str)

def converter_entrada_para_indices(jogada_user, tamanho_tabuleiro):
    coluna_char = jogada_user[0].upper()
    linha_str = jogada_user[1:]

    if not coluna_char.isalpha() or not linha_str.isdigit():  # validacao
        print("Entrada inválida. Digite uma célula válida (por exemplo, A1 ou !mostrar).")
        return None, None

    coluna = ord(coluna_char) - ord('A')
    linha = int(linha_str)

    if not (0 <= coluna < tamanho_tabuleiro[1]) or not (0 <= linha < tamanho_tabuleiro[0]):
        print("Célula fora dos limites. Digite uma célula válida (por exemplo, A1 ou !mostrar).")
        return None, None

    return linha, coluna

def atacar_navio(tabuleiro, linha, coluna, posicoes_navios):
    posicao_atual = tabuleiro[linha][coluna]

    if isinstance(posicao_atual, int) and (linha, coluna) in posicoes_navios:
        posicoes_navios.remove((linha, coluna))

        if not posicoes_navios:
            print("Você conseguiu destruir o navio!")
            return True
    else:
        print("Tiro na água. Tente novamente.")

    return False

def mostrar_todos_navios(tabuleiro, posicoes_navios):
    for posicao in posicoes_navios:
        linha, coluna = posicao
        tabuleiro[linha][coluna] = str(len(posicoes_navios) + 1)

def main():
    # Definindo tabuleiros para os dois jogadores
    jogador1_tabuleiro, jogador1_posicoes_navios = criar_tabuleiro(8, 8, 10)
    jogador2_tabuleiro, jogador2_posicoes_navios = criar_tabuleiro(8, 8, 10)

    jogador1_revelado = [[False for _ in range(8)] for _ in range(8)]
    jogador2_revelado = [[False for _ in range(8)] for _ in range(8)]

    vez_jogador1 = True

    while True:
        # Alternando entre os jogadores
        if vez_jogador1:
            jogador = {
                'tabuleiro': jogador1_tabuleiro,
                'posicoes_navios': jogador1_posicoes_navios,
                'revelado': jogador1_revelado
            }
            outro_jogador = {
                'tabuleiro': jogador2_tabuleiro,
                'posicoes_navios': jogador2_posicoes_navios,
                'revelado': jogador2_revelado
            }
        else:
            jogador = {
                'tabuleiro': jogador2_tabuleiro,
                'posicoes_navios': jogador2_posicoes_navios,
                'revelado': jogador2_revelado
            }
            outro_jogador = {
                'tabuleiro': jogador1_tabuleiro,
                'posicoes_navios': jogador1_posicoes_navios,
                'revelado': jogador1_revelado
            }

        print(f"{'Jogador 1' if vez_jogador1 else 'Jogador 2'}'s Turno:")
        imprimir_tabuleiro(jogador['tabuleiro'], jogador['revelado'])

        entrada = input("Digite a célula a ser atacada (por exemplo, A1) ou !mostrar para revelar os navios: ")

        if entrada.lower() == "!mostrar":
            mostrar_todos_navios(jogador['tabuleiro'], jogador['posicoes_navios'])
            imprimir_tabuleiro(jogador['tabuleiro'], jogador['revelado'])
            break

        linha, coluna = converter_entrada_para_indices(entrada, (8, 8))

        if linha is None or coluna is None:
            continue  # Volta ao início do loop para pedir uma nova entrada

        if jogador['revelado'][linha][coluna]:
            print("Célula já revelada. Escolha outra célula.")
            continue

        jogador['revelado'][linha][coluna] = True

        if atacar_navio(jogador['tabuleiro'], linha, coluna, jogador['posicoes_navios']):
            imprimir_tabuleiro(jogador['tabuleiro'], jogador['revelado'])
            print(f"Parabéns! {'Jogador 1' if vez_jogador1 else 'Jogador 2'} destruiu todos os navios inimigos. "
                  f"{'Jogador 1' if vez_jogador1 else 'Jogador 2'} venceu!")
            break

        # Troca para o próximo jogador
        vez_jogador1 = not vez_jogador1

if __name__ == "__main__":
    main()
