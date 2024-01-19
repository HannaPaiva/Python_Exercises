
vencedor = 0

def criar_tabuleiro(tamanho):

    return [['.' for _ in range(tamanho)] for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro):

    colunas = " ".join(chr(ord('A') + i) for i in range(len(tabuleiro)))
    print(f"  {colunas}")
    for i, linha in enumerate(tabuleiro):

        print(f"{i} {' '.join(linha)}")


def imprimir_tabuleiro_oculto(tabuleiro):

    colunas = " ".join(chr(ord('A') + i) for i in range(len(tabuleiro)))

    print(f"  {colunas}")

    for i, linha in enumerate(tabuleiro):

        print(f"{i} {' '.join('.' if celula == 'S' else celula for celula in linha)}")

def converter_coordenadas(coord, tamanho_tabuleiro):
    try:
        x = int(coord[1])
        y = ord(coord[0].upper()) - ord('A')


        if 0 <= x < tamanho_tabuleiro and 0 <= y < tamanho_tabuleiro:
            return x, y
        else:
            print("Coordenada fora do tabuleiro. Tente novamente.")
            return converter_coordenadas(input("Digite a coordenada (ex: A0): "), tamanho_tabuleiro)
        
    except (ValueError, IndexError):
        print("Entrada inválida. Tente novamente.")

        return converter_coordenadas(input("Digite a coordenada (ex: A0): "), tamanho_tabuleiro)
    

def colocar_navio(tabuleiro, inicio, fim):
    x1, y1 = inicio

    x2, y2 = fim
    if x1 == x2:
        for y in range(y1, y2 + 1):

            tabuleiro[x1][y] = 'S'
    else:
        for x in range(x1, x2 + 1):

            tabuleiro[x][y1] = 'S'

def configurar_jogador(tabuleiro, jogador, tamanho_navio):

    imprimir_tabuleiro(tabuleiro)

    coord = input(f"Jogador {jogador}, onde deseja colocar o seu navio de {tamanho_navio} posições? (ex: A0): ")

    x, y = converter_coordenadas(coord, len(tabuleiro))

    orientacao = int(input("1. Para colocar na horizontal\n2. Para colocar na vertical\nEscolha a orientação: "))

    if orientacao == 1:
        fim_y = y + tamanho_navio - 1

        if 0 <= fim_y < len(tabuleiro[0]):

            colocar_navio(tabuleiro, (x, y), (x, fim_y))
        else:
            print("Posição inválida. Tente novamente.")
            configurar_jogador(tabuleiro, jogador, tamanho_navio)

    elif orientacao == 2:
        fim_x = x + tamanho_navio - 1
        if 0 <= fim_x < len(tabuleiro):

            colocar_navio(tabuleiro, (x, y), (fim_x, y))
        else:

            print("Posição inválida. Tente novamente.")

            configurar_jogador(tabuleiro, jogador, tamanho_navio)
    else:
        print("Escolha inválida. Tente novamente.")

        configurar_jogador(tabuleiro, jogador, tamanho_navio)


def atirar(tabuleiro, x, y):

    if tabuleiro[x][y] == 'S':

        tabuleiro[x][y] = 'X'

        print("Acertou!")

        return True
    
    elif tabuleiro[x][y] == '.':

        tabuleiro[x][y] = ' '

        print("Errou!")
        return False
    else:
        print("Você já atirou aqui. Tente novamente.")
        return False

def resetar_jogo():
    return criar_tabuleiro(8), criar_tabuleiro(8)

def jogar_batalha_naval():
    tamanho_tabuleiro = 8
    tabuleiro_jogador1, tabuleiro_jogador2 = resetar_jogo()

    # Jogadores colocam seus navios
    configurar_jogador(tabuleiro_jogador1, 1, 5) #1 navio de 5
    configurar_jogador(tabuleiro_jogador1, 1, 4) #1 navio de 4
    configurar_jogador(tabuleiro_jogador1, 1, 3) #2 navios de 3
    configurar_jogador(tabuleiro_jogador1, 1, 3)
    configurar_jogador(tabuleiro_jogador1, 1, 2) #1 navio de 2

    #repete para o outro player
    configurar_jogador(tabuleiro_jogador2, 2, 5)
    configurar_jogador(tabuleiro_jogador2, 2, 4)
    configurar_jogador(tabuleiro_jogador2, 2, 3)
    configurar_jogador(tabuleiro_jogador2, 2, 3)
    configurar_jogador(tabuleiro_jogador2, 2, 2)

    jogador_atual = 1

    # Jogadores atiranod
    while True:
        imprimir_tabuleiro(tabuleiro_jogador1) if jogador_atual == 1 else imprimir_tabuleiro_oculto(tabuleiro_jogador1)
        imprimir_tabuleiro(tabuleiro_jogador2) if jogador_atual == 2 else imprimir_tabuleiro_oculto(tabuleiro_jogador2)

        print(f"Jogador {jogador_atual}, atire!")
        coord = input("Digite a coordenada (ex: A0): ")
        x, y = converter_coordenadas(coord, tamanho_tabuleiro)

        if jogador_atual == 1:
            acerto = atirar(tabuleiro_jogador2, x, y)
            if 'S' not in sum(tabuleiro_jogador2, []):
                print("Jogador 1 ganhou!")
                vencedor = 1
                return vencedor
        else:
            acerto = atirar(tabuleiro_jogador1, x, y)
            if 'S' not in sum(tabuleiro_jogador1, []):
                print("Jogador 2 ganhou!")
                vencedor = 2
                return vencedor

        if not acerto:
            jogador_atual = 3 - jogador_atual  # Troca de jogador

if __name__ == "__main__":
    jogar_batalha_naval()
     