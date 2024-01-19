# Importar o módulo json para ler e escrever arquivos json
import json

# Definir uma função para desenhar o tabuleiro
def desenhar_tabuleiro(tabuleiro):
    print("---|---|---")
    print(" " + tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2])
    print("---|---|---")
    print(" " + tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5])
    print("---|---|---")
    print(" " + tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8])

# Definir uma função para limpar o tabuleiro
def limpar_tabuleiro():
    return [" "]*9

# Definir uma função para verificar se há um vencedor
def verificar_vencedor(tabuleiro):
    # Verificar as linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] and tabuleiro[i] != " ":
            return tabuleiro[i]
    # Verificar as colunas
    for j in range(3):
        if tabuleiro[j] == tabuleiro[j+3] == tabuleiro[j+6] and tabuleiro[j] != " ":
            return tabuleiro[j]
    # Verificar as diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] and tabuleiro[0] != " ":
        return tabuleiro[0]
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] and tabuleiro[2] != " ":
        return tabuleiro[2]
    # Verificar se há empate
    if " " not in tabuleiro:
        return "empate"
    # Caso contrário, o jogo ainda não acabou
    return None

# Definir uma função para obter a jogada válida de um jogador
def obter_jogada(jogador, tabuleiro):
    while True:
        try:
            jogada = int(input(f"{jogador}, escolha uma posição (1-9): ")) - 1
            if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                return jogada
            else:
                print("Posição inválida ou já ocupada. Escolha novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 9.")

# Definir uma função para jogar o jogo da velha
def jogar_velha(jogador1, jogador2):
    # Inicializar as variáveis
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    vitorias_jogador1 = 0
    vitorias_jogador2 = 0
    nome_jogo = "velha"
    arquivo_json = "resultado.json"

    # Ler o arquivo json se existir e atualizar as variáveis
    try:
        with open(arquivo_json, "r") as f:
            resultado = json.load(f)
            for jogo in resultado:
                if jogo["nomejogo"] == nome_jogo:
                    vitorias_jogador1 = jogo["vitoriasjg1"]
                    vitorias_jogador2 = jogo["vitoriasjg2"]
                    break
    except FileNotFoundError:
        resultado = []

    # Iniciar o loop principal do jogo
    while True:
        # Criar um novo tabuleiro
        tabuleiro = limpar_tabuleiro()
        # Definir o primeiro jogador como X
        jogador = "X"
        # Iniciar o loop de uma partida
        while True:
            # Mostrar o tabuleiro
            desenhar_tabuleiro(tabuleiro)
            # Obter a jogada do jogador
            jogada = obter_jogada(jogador, tabuleiro)
            # Marcar a jogada no tabuleiro
            tabuleiro[jogada] = jogador
            # Verificar se há um vencedor
            vencedor = verificar_vencedor(tabuleiro)
            if vencedor is not None:
                # Mostrar o tabuleiro final
                desenhar_tabuleiro(tabuleiro)
                # Anunciar o resultado
                if vencedor == "empate":
                    print("Empate!")
                else:
                    print(f"{jogador} venceu!")
                    # Atualizar os pontos do vencedor
                    if jogador == "X":
                        pontos_jogador1 += 1
                    else:
                        pontos_jogador2 += 1
                # Encerrar a partida
                break
            # Trocar o jogador
            jogador = "O" if jogador == "X" else "X"
        # Mostrar os pontos de cada jogador
        print(f"\nPontos de {jogador1}: {pontos_jogador1} pontos")
        print(f"Pontos de {jogador2}: {pontos_jogador2} pontos")
        # Verificar se alguém ganhou o melhor de 3
        if pontos_jogador1 == 3 or pontos_jogador2 == 3:
            # Anunciar o vencedor do melhor de 3
            if pontos_jogador1 == 3:
                print(f"{jogador1} ganhou o melhor de 3!")
                # Atualizar as vitórias do jogador 1
                vitorias_jogador1 += 1
            else:
                print(f"{jogador2} ganhou o melhor de 3!")
                # Atualizar as vitórias do jogador 2
                vitorias_jogador2 += 1
            # Mostrar as vitórias de cada jogador
            print(f"\nVitórias de {jogador1}: {vitorias_jogador1} vitórias")
            print(f"Vitórias de {jogador2}: {vitorias_jogador2} vitórias")
            # Zerar os pontos de cada jogador
            pontos_jogador1 = 0
            pontos_jogador2 = 0
        # Perguntar se os jogadores querem jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            # Atualizar o arquivo json com o resultado do jogo
            jogo_atualizado = False
            for jogo in resultado:
                if jogo["nomejogo"] == nome_jogo:
                    jogo["jogador1"] = jogador1
                    jogo["jogador2"] = jogador2
                    jogo["vitoriasjg1"] = vitorias_jogador1
                    jogo["vitoriasjg2"] = vitorias_jogador2
                    jogo["pontosjg1"] = pontos_jogador1
                    jogo["pontosjg2"] = pontos_jogador2
                    jogo_atualizado = True
                    break
            if not jogo_atualizado:
                resultado.append({
                    "nomejogo": nome_jogo,
                    "jogador1": jogador1,
                    "jogador2": jogador2,
                    "vitoriasjg1": vitorias_jogador1,
                    "vitoriasjg2": vitorias_jogador2,
                    "pontosjg1": pontos_jogador1,
                    "pontosjg2": pontos_jogador2
                })
            with open(arquivo_json, "w") as f:
                json.dump(resultado, f, indent=4)
            # Encerrar o jogo
            break

if __name__ == "__main__":
    # Pedir o nome dos jogadores
    jogador1 = input("Digite o nome do Jogador 1: ")
    jogador2 = input("Digite o nome do Jogador 2: ")
    # Jogar o jogo da velha
    jogar_velha(jogador1, jogador2)
