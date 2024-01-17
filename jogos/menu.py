import json
import os.path
import gloria as gloria
import forca as forca

import quatro_em_linha as quatro_em_linha

import batalha_naval as batalha_naval
import batalha_naval_computador as batalha_naval_computador

import campo_minado as campo_minado

import velha as velha
import velha_computador as velha_computador

def jogo_4_em_linha():
    quatro_em_linha.jogar_quatro_em_linha()
   

def jogo_batalha_naval():
    
    while True:
        resultado = batalha_naval.jogar_batalha_naval()
        print(f"Jogador vencedor: {resultado}")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            return resultado 
        else:
            batalha_naval.reset_game()
   

def jogo_da_velha():
    while True:
        resultado = velha.jogar_velha()
        print(f"Jogador vencedor: {resultado}")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            return resultado  # Retorna o resultado se o jogador não quiser jogar novamente
        else:
            velha.limpar_tabuleiro()

def jogar_velha_computador():
    while True:
        resultado = velha_computador.jogar_velha()
        print(f"Jogador vencedor: {resultado}")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            return resultado  # Retorna o resultado se o jogador não quiser jogar novamente

def jogo_forca():
    forca.jogar_forca()
    pass

def jogo_gloria():
    gloria.jogar_gloria()

def jogo_campo_minado():
    campo_minado.jogar_campo_minado()
    pass

def carregar_dados_jogos():
    if os.path.exists("historico_jogos.json"):
        with open("historico_jogos.json", "r") as file:
            return json.load(file)
    return []

def salvar_dados_jogos(dados_jogos):
    with open("historico_jogos.json", "w") as file:
        json.dump(dados_jogos, file, indent=2)

def atualizar_scores(dados_jogos, jogador1, jogador2, resultado):
    vitorias_jg1 = sum(jogo["vitoriasjg1"] for jogo in dados_jogos if jogo["jogador1"] == jogador1)
    vitorias_jg2 = sum(jogo["vitoriasjg2"] for jogo in dados_jogos if jogo["jogador2"] == jogador2)

    if vitorias_jg1 > vitorias_jg2:
        return 3 * vitorias_jg1, 0
    elif vitorias_jg2 > vitorias_jg1:
        return 0, 3 * vitorias_jg2
    else:
        return vitorias_jg1, vitorias_jg2

def jogar_computador(opcao_jogo):
    if opcao_jogo == "1":  # Jogo da Velha
        return jogar_velha_computador()
    elif opcao_jogo == "2":
        # Adicione a lógica para outros jogos
        resultado = 0  # Simples exemplo de um jogo fictício
        print(f"Jogador vencedor: {resultado}")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            return resultado  
    else:
        resultado = 0
        print(f"Jogador vencedor: {resultado}")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            return resultado  # Retorna o resultado se o jogador não quiser jogar novamente

def main():
    dados_jogos = carregar_dados_jogos()

    while True:
        print("\nMenu de Jogos:")
        print("1. Jogo da Velha")
        print("2. 4 em Linha")
        print("3. Batalha Naval")
        print("4. Forca")
        print("5. Campo minado")
        print("6. Glória")
        print("10. Visualizar histórico de jogos")
        print("x. Sair")

        opcao_jogo = input("Escolha um jogo: ")

        if opcao_jogo in ["1", "2", "3", "4", "5", "6"]:
            jogador1 = input("Digite o nome do Jogador 1: ")

            modo_jogo = input("Escolha o modo de jogo (1 para 2 jogadores, 2 para jogar contra o computador): ")

            if modo_jogo == "1":
                jogador2 = input("Digite o nome do Jogador 2: ")
            else:
                jogador2 = "Computador"

            if modo_jogo == "2":
                resultado = jogar_computador(opcao_jogo)
            else:
                if opcao_jogo == "1":
                    resultado = jogo_da_velha()  # retorna 1 se o jogador 1 ganhou, 2 se o jogador 2 ganhou, 0 se foi empate
                elif opcao_jogo == "2":
                    jogo_4_em_linha()
                elif opcao_jogo == "3":
                    jogo_batalha_naval()
                elif opcao_jogo == "4":
                    jogo_forca()
                elif opcao_jogo == "5":
                    jogo_campo_minado()
                elif opcao_jogo == "6":
                    jogo_gloria()

                nomejogo = "velha"  # Ou adapte conforme o jogo selecionado

                # Registrar o resultado do jogo no histórico
                pontos_jg1, pontos_jg2 = atualizar_scores(dados_jogos, jogador1, jogador2, resultado)
                dados_jogos.append({"nomejogo": nomejogo, "jogador1": jogador1, "jogador2": jogador2,
                                    "vitoriasjg1": int(resultado == 1), "vitoriasjg2": int(resultado == 2),
                                    "pontosjg1": pontos_jg1, "pontosjg2": pontos_jg2})

                salvar_dados_jogos(dados_jogos)

                print(f"\nPontos de {jogador1}: {pontos_jg1} pontos")
                print(f"Pontos de {jogador2}: {pontos_jg2} pontos")

        elif opcao_jogo == "10":
            print("Histórico de Jogos:")
            print(json.dumps(dados_jogos, indent=2))
        elif opcao_jogo.lower() == "x":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
