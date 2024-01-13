import random

def criar_tabuleiro(linhas, colunas, num_navios):

    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]

    posicoes_navios = random.sample(range(linhas * colunas), num_navios)

    for posicao in posicoes_navios:
        linha = posicao // colunas
        coluna = posicao % colunas
        tabuleiro[linha][coluna] = 'N'

    return tabuleiro, posicoes_navios

def imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=False):
    cabecalho = "  " + " ".join(chr(65 + col) for col in range(len(tabuleiro[0])))
    print(cabecalho)

    for linha, dados_linha in enumerate(tabuleiro):
        linha_str = f"{linha} "

        for coluna, dados_coluna in enumerate(dados_linha):

            if mostrar_navios and tabuleiro[linha][coluna] == 'N':
                linha_str += 'N '
            elif revelado[linha][coluna]:
                linha_str += dados_coluna + " "
            else:
                linha_str += ". "
        print(linha_str)

def contar_navios_adjacentes(tabuleiro, linha, coluna):
    count = 0

    for i in range(max(0, linha - 1), min(linha + 2, len(tabuleiro))):
        for j in range(max(0, coluna - 1), min(coluna + 2, len(tabuleiro[0]))):
            if tabuleiro[i][j] == 'N':
                count += 1
    return count

def revelar_celula(tabuleiro, revelado, linha, coluna):

    if revelado[linha][coluna]:
        return False

    revelado[linha][coluna] = True

    if tabuleiro[linha][coluna] == 'N':
        imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=True)
        print("Você atingiu um navio!")
        return False
    else:
        navios_proximos = contar_navios_adjacentes(tabuleiro, linha, coluna)
        tabuleiro[linha][coluna] = str(navios_proximos) if navios_proximos > 0 else ' '
        return False

def mostrar_navios(tabuleiro, posicoes_navios):
    
    for posicao in posicoes_navios:
        linha = posicao // len(tabuleiro[0])
        coluna = posicao % len(tabuleiro[0])
        tabuleiro[linha][coluna] = 'N'

def verificar_vitoria(revelado, num_navios):
    return sum(row.count(True) for row in revelado) == (len(revelado) * len(revelado[0]) - num_navios)

def main():

    linhas = 8
    colunas = 8
    num_navios = 10

    tabuleiro, posicoes_navios = criar_tabuleiro(linhas, colunas, num_navios)

    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]
    navios_mostrados = False

    while True:

        if navios_mostrados:
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=True)
        else:
            imprimir_tabuleiro(tabuleiro, revelado)

        entrada = input("Digite a célula a ser revelada (por exemplo, A1) ou !mostrar para revelar os navios: ")

        if entrada.lower() == "!mostrar":
            navios_mostrados = True
            mostrar_navios(tabuleiro, posicoes_navios)
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=True)
            break

        linha, coluna = converter_entrada_para_indices(entrada, (linhas, colunas))

        if linha is None or coluna is None:
            continue  

        if revelar_celula(tabuleiro, revelado, linha, coluna):
            navios_mostrados = True
            mostrar_navios(tabuleiro, posicoes_navios)
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=True)
            print("Você atingiu um navio!")
            break

        if verificar_vitoria(revelado, num_navios):
            navios_mostrados = True
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_navios=True)
            print("Parabéns! Você destruiu todos os navios!")
            break

def converter_entrada_para_indices(jogada_user, tamanho_tabuleiro):

    coluna_char = jogada_user[0].upper()
    linha_str = jogada_user[1:]

    if not coluna_char.isalpha() or not linha_str.isdigit():
        print("Entrada inválida. Digite uma célula válida (por exemplo, A1) ou !mostrar para revelar os navios.")
        return None, None

    coluna = ord(coluna_char) - ord('A')

    linha = int(linha_str)

    if not (0 <= coluna < tamanho_tabuleiro[1]) or not (0 <= linha < tamanho_tabuleiro[0]):
        print("Célula fora dos limites. Digite uma célula válida (por exemplo, A1) ou !mostrar para revelar os navios.")
        return None, None

    return linha, coluna

if __name__ == "__main__":
    main()
