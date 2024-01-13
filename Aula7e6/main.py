import jogos.velha as velha
import jogos.quatro_em_linha as quatro_em_linha
import pyfiglet
import curses
import time
import piscar_menu

def main_menu():
    ascii_art = pyfiglet.figlet_format("Menu de Jogos")
    ascii_art_2 = pyfiglet.figlet_format("Escolha o jogo")
    print(ascii_art)
    print(ascii_art_2)
    print("Selecione um jogo:")
    print("1. Jogo da Velha")
    print("2. Quatro em Linha")
    print("3. Jogo da Glória")
    print("4. Sair")

    choice = input("Escolha o número do jogo ou '4' para sair: ")
    if choice == "1":
        start_game("Jogo da Velha")
    elif choice == "2":
        start_game("Quatro em Linha")
    elif choice == "3":
        start_game("Jogo da Glória")
    elif choice == "4":
        quit_game_menu()
    else:
        print("Escolha inválida. Tente novamente.")
        main_menu()

def start_game(game_name):
    print(f"Iniciando {game_name}...")

def quit_game_menu():
    print("Saindo do menu de seleção de jogos.")



main_menu()