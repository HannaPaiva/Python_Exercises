import random

def create_board(size):
    return [['.' for _ in range(size)] for _ in range(size)]

def print_board(board):
    columns = " ".join(chr(ord('A') + i) for i in range(len(board)))
    print(f"  {columns}")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def print_hidden_board(board):
    columns = " ".join(chr(ord('A') + i) for i in range(len(board)))
    print(f"  {columns}")
    for i, row in enumerate(board):
        print(f"{i} {' '.join('.' if cell == 'S' else cell for cell in row)}")

def convert_coordinates(coord):
    x = int(coord[1:])
    y = ord(coord[0].upper()) - ord('A')
    return x, y

def place_ship(board, start, end):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        for y in range(y1, y2 + 1):
            board[x1][y] = 'S'
    else:
        for x in range(x1, x2 + 1):
            board[x][y1] = 'S'

def player_setup(board, player, ship_size):
    print_board(board)
    for _ in range(ship_size):
        while True:
            coord = input(f"Jogador {player}, aonde deseja colocar o seu barco de {ship_size} posições? (ex: A0): ")
            x, y = convert_coordinates(coord)

            orientation = int(input("1. Para colocar na horizontal\n2. Para colocar na vertical\nEscolha a orientação: "))

            if orientation == 1:
                end_y = y + ship_size - 1
                if 0 <= end_y < len(board[0]) and all(board[x][i] == '.' for i in range(y, end_y + 1)):
                    place_ship(board, (x, y), (x, end_y))
                    break
            elif orientation == 2:
                end_x = x + ship_size - 1
                if 0 <= end_x < len(board) and all(board[i][y] == '.' for i in range(x, end_x + 1)):
                    place_ship(board, (x, y), (end_x, y))
                    break
            else:
                print("Escolha inválida. Tente novamente.")

def computer_setup(board, player, ship_size):
    for _ in range(ship_size):
        while True:
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board[0]) - 1)
            orientation = random.choice([1, 2])

            if orientation == 1:
                end_y = y + ship_size - 1
                if 0 <= end_y < len(board[0]) and all(board[x][i] == '.' for i in range(y, end_y + 1)):
                    place_ship(board, (x, y), (x, end_y))
                    break
            elif orientation == 2:
                end_x = x + ship_size - 1
                if 0 <= end_x < len(board) and all(board[i][y] == '.' for i in range(x, end_x + 1)):
                    place_ship(board, (x, y), (end_x, y))
                    break

def computer_input(board):
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board[0]) - 1)
    return x, y

def shoot(board, x, y):
    if board[x][y] == 'S':
        board[x][y] = 'X'
        print("Acertou!")
        return True
    elif board[x][y] == '.':
        board[x][y] = ' '
        print("Errou!")
        return False
    else:
        print("Você já atirou aqui. Tente novamente.")
        return False

def check_game_over(board):
    return all(cell != 'S' for row in board for cell in row)

def jogar_batalha_naval_computador():
    board_size = 8
    player1_board = create_board(board_size)
    player2_board = create_board(board_size)

    # Jogadores colocam seus navios
    player_setup(player1_board, 1, 5)
    computer_setup(player2_board, 2, 5)

    # Jogadores atiram um no outro
    current_player = 1
    while True:
        if current_player == 1:
            print_board(player1_board)
            print_hidden_board(player2_board)
        else:
            print_hidden_board(player1_board)
            print_board(player2_board)

        print(f"Jogador {current_player}, atire!")

        if current_player == 1:
            coord = input("Digite a coordenada (ex: A0): ")
            x, y = convert_coordinates(coord)
        else:
            x, y = computer_input(player2_board)

        if 0 <= x < len(player1_board) and 0 <= y < len(player1_board[0]) and \
           0 <= x < len(player2_board) and 0 <= y < len(player2_board[0]):
            if current_player == 1:
                hit = shoot(player2_board, x, y)
                if check_game_over(player2_board):
                    print("Jogador 1 ganhou!")
                    break
            else:
                hit = shoot(player1_board, x, y)
                if check_game_over(player1_board):
                    print("Jogador 2 (computador) ganhou!")
                    break
        else:
            print("Coordenada inválida. Tente novamente.")

        if not hit:
            current_player = 3 - current_player  # Troca de jogador

if __name__ == "__main__":
    jogar_batalha_naval_computador()
