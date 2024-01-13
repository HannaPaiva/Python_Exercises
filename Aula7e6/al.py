# main.py
import json
import random
from jogos.quatro_em_linha import *
from jogos.campo_minado import *
from batalha_naval import *

def menu():
    print("1. Jogo 4 em Linha")
    print("2. Jogo Campo de Minas")
    print("3. Jogo Batalha Naval")
    escolha = input("Escolha um jogo (1-3): ")
    return escolha

def salvar(jogadores):
    with open('jogo.json', 'w') as f:
        json.dump(jogadores, f)

def carregar():
    try:
        with open('jogo.json', 'r') as f:
            jogadores = json.load(f)
            print("Jogadores carregados:")
            for jogador, pontuacao in jogadores.items():
                print(f"{jogador}: {pontuacao} pontos")
    except FileNotFoundError:
        jogadores = {}
    return jogadores

def main():
    jogadores = carregar()

    while True:
        escolha_jogo = menu()

        if escolha_jogo == '1':
            jogar_connect_four(jogadores)
        elif escolha_jogo == '2':
            jogar_campo_minas(jogadores)
        elif escolha_jogo == '3':
            jogar_batalha_naval(jogadores)
        else:
            print("Opção inválida. Saindo do programa.")
            break

        if "Jogador 1" not in jogadores:
            jogadores["Jogador 1"] = 0
        if "Jogador 2" not in jogadores:
            jogadores["Jogador 2"] = 0

        salvar(jogadores)

if __name__ == "__main__":
    main()
