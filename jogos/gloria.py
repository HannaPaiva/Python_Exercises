import json
import random

def mover(tabuleiro, turno):
    espacos = random.randint(1, 6)  # dado de 1 a 6
    print(f"Jogador {turno + 1} lançou {espacos} no dado.")
    tabuleiro[turno] += espacos


    if tabuleiro[turno] >= 30:

        print(f"Jogador {turno + 1} ganhou!")
        tabuleiro = [0, 0]
    else:
        # ações/consequências ao cair em certas casas
        if tabuleiro[turno] in [3, 9, 15, 21, 27]:
            print(f"Jogador {turno + 1} caiu em uma casa especial e avança 2 casas!")


            tabuleiro[turno] += 2
        elif tabuleiro[turno] in [5, 10, 20, 25]:

            print(f"Jogador {turno + 1} caiu em uma casa especial e retrocede 3 casas!")
            tabuleiro[turno] -= 3
    turno = 1 - turno  # troca de jogador
    return tabuleiro, turno

def salvar(tabuleiro):

    with open('gloria.json', 'w') as f:
        json.dump(tabuleiro, f)

def carregar():
    try:
        with open('gloria.json', 'r') as f:
            tabuleiro = json.load(f)

            print(f"O jogador X estava na posição {tabuleiro[0]}, O jogador O estava na posição {tabuleiro[1]}")


    except FileNotFoundError:
        tabuleiro = [0, 0]
    return tabuleiro

def menu():
    print("Jogo da Glória! ")

    print("1. Começar um novo jogo")
    print("2. Carregar o jogo anterior")
    escolha = input("Escolha uma opção: ")



    if escolha == '1':

        tabuleiro = [0, 0]
    elif escolha == '2':

        tabuleiro = carregar()
    else:
        print("Opção inválida. Começando um novo jogo...")
        tabuleiro = [0, 0]
    return tabuleiro

def desenhar_tabuleiro(tabuleiro):
    print('+---' * 31 + '+')
    for i in range(30):
        if i == tabuleiro[0] and i == tabuleiro[1]:

            print('|X*O', end='')

        elif i == tabuleiro[0]:
            print('| X ', end='')

        elif i == tabuleiro[1]:
            print('| O ', end='')

        else:
            print('|   ', end='')
    print('|')
    print('+---' * 30 + '+')

def jogar_gloria():
    tabuleiro = menu()
    turno = 0

    while True:
        desenhar_tabuleiro(tabuleiro)
        
        entrada_movimento = input(f"Jogador {turno + 1}, pressione enter para lançar o dado ou digite 'sair' para sair: ")

        if entrada_movimento.lower() == 'sair':
            salvar(tabuleiro)
            break
        tabuleiro, turno = mover(tabuleiro, turno)

if __name__ == "__main__":
    jogar_gloria()
