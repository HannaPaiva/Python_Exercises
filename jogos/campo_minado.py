import random
''' 
Jogo do campo minado:pode receber params de criar o tabuleiro com a quantidade de cada coisa (linha, coluna e número de bombas)

MAS!! BUT!! PORÉM!! Lembrar: O máximo de colunas é a quantidade total de letras no alfabeto se não aparece uns simbolos estranhos.

'''
def criar_tabuleiro(linhas, colunas, num_bombas):

    # tabuleiro = [[0 for _ in range(8)] for _ in range(8)]

    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]


    posicoes_bombas = random.sample(range(linhas * colunas), num_bombas) # bombas aleatórias (lista)

    for posicao in posicoes_bombas:

        linha = posicao // colunas #(parte inteira do resultado da divisao)
        coluna = posicao % colunas #

        tabuleiro[linha][coluna] = 'B'

    return tabuleiro, posicoes_bombas




def imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=False):
    cabecalho = "  " + " ".join(chr(65 + col) for col in range(len(tabuleiro[0]))) # LETRAS/COLUNAS
    print(cabecalho)

    for linha, dados_linha in enumerate(tabuleiro): # cada linha da matriz // valor + índice
        linha_str = f"{linha} "

        for coluna, dados_coluna in enumerate(dados_linha): # cada coluna 

            if mostrar_bombas and tabuleiro[linha][coluna] == 'B':
                linha_str += 'B '
            elif revelado[linha][coluna]:
                linha_str += dados_coluna + " " # ESCOLHIDO --> REVELAR
            else:
                linha_str += ". "
        print(linha_str)

def converter_entrada_para_indices(jogada_user, tamanho_tabuleiro):

    coluna_char = jogada_user[0].upper()
    linha_str = jogada_user[1:] #pode ser numero com 2 digitos aq

    if not coluna_char.isalpha() or not linha_str.isdigit(): # validacao
        print("Entrada inválida. Digite uma célula válida (por exemplo, A1) ou !mostrar para revelar as bombas.")
        return None, None
    

    coluna = ord(coluna_char) - ord('A')

    linha = int(linha_str)

    if not (0 <= coluna < tamanho_tabuleiro[1]) or not (0 <= linha < tamanho_tabuleiro[0]):

        print("Célula fora dos limites. Digite uma célula válida (por exemplo, A1) ou !mostrar para revelar as bombas.")
        return None, None

    return linha, coluna

#CHATGPT 
def contar_bombas_adjacentes(tabuleiro, linha, coluna):
    count = 0

    for i in range(max(0, linha - 1), min(linha + 2, len(tabuleiro))):

        for j in range(max(0, coluna - 1), min(coluna + 2, len(tabuleiro[0]))):

            if tabuleiro[i][j] == 'B':
                count += 1
    return count

def revelar_celula(tabuleiro, revelado, linha, coluna):

    if revelado[linha][coluna]:
        return False #salta fora

    revelado[linha][coluna] = True

    if tabuleiro[linha][coluna] == 'B': # se escolheu a bomba

        imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=True)
        print("Você perdeu! Uma bomba foi detonada.")
        return True
    
    else:
        # se acertou, conta adjacentes 
        bombas_proximas = contar_bombas_adjacentes(tabuleiro, linha, coluna)
        tabuleiro[linha][coluna] = str(bombas_proximas) if bombas_proximas > 0 else ' '
        return False

def mostrar_bombas(tabuleiro, posicoes_bombas):
    
    for posicao in posicoes_bombas:
        linha = posicao // len(tabuleiro[0])
        coluna = posicao % len(tabuleiro[0])
        tabuleiro[linha][coluna] = 'B'

def verificar_vitoria(revelado, num_bombas):
    # verifica se cada posicao não contendo bombas foi revelada
    return sum(row.count(True) for row in revelado) == (len(revelado) * len(revelado[0]) - num_bombas)


def main():

    linhas = 8
    colunas = 8
    num_bombas = 10


    tabuleiro, posicoes_bombas = criar_tabuleiro(linhas, colunas, num_bombas)

    revelado = [[False for _ in range(colunas)] for _ in range(linhas)] #todas as posicoes ja reveladas.
    bombas_mostradas = False

    while True:

        if bombas_mostradas:
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=True)
        else:
            imprimir_tabuleiro(tabuleiro, revelado)

        entrada = input("Digite a célula a ser revelada (por exemplo, A1) ou !mostrar para revelar as bombas: ")

        if entrada.lower() == "!mostrar":
            bombas_mostradas = True
            mostrar_bombas(tabuleiro, posicoes_bombas)
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=True)
            break

        linha, coluna = converter_entrada_para_indices(entrada, (linhas, colunas))

        if linha is None or coluna is None:
            continue  # Volta ao início do loop para pedir uma nova entrada

        if revelar_celula(tabuleiro, revelado, linha, coluna):
            bombas_mostradas = True
            mostrar_bombas(tabuleiro, posicoes_bombas)
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=True)
            print("Você perdeu! Uma bomba foi detonada.")
            break

        if verificar_vitoria(revelado, num_bombas):
            bombas_mostradas = True
            imprimir_tabuleiro(tabuleiro, revelado, mostrar_bombas=True)
            print("Parabéns! Você venceu!")
            break

if __name__ == "__main__":
    main()
