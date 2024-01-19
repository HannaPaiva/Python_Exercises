import json

def verificar_vencedor(tabuleiro):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " ":
            return tabuleiro[i][0]
    for j in range(3):
        if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] and tabuleiro[0][j] != " ":
            return tabuleiro[0][j]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return None
    return "empate"

def mostrar_tabuleiro(tabuleiro):
    print(" " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("---+---+---")
    print(" " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("---+---+---")
    print(" " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])

def salvar_progresso(jogador1, jogador2, tabuleiro, turno, pontos_jogador1, pontos_jogador2):
    dados = {
        "jogador1": jogador1,
        "jogador2": jogador2,
        "tabuleiro": tabuleiro,
        "turno": turno,
        "pontos_jogador1": pontos_jogador1,
        "pontos_jogador2": pontos_jogador2
    }
    with open("progresso.json", "w") as arquivo:
        json.dump(dados, arquivo)

def carregar_progresso():
    with open("progresso.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados

def atualizar_resultado(jogador1, jogador2, ponto1, ponto2, vitorias_jogador1, vitorias_jogador2):
    with open("resultado.json", "r") as arquivo:
        lista_resultados = json.load(arquivo)

    encontrado = False
    for resultado in lista_resultados:
        if resultado["nomejogo"] == "velha" and resultado["jogador1"] == jogador1 and resultado["jogador2"] == jogador2:
            encontrado = True
            resultado["vitoriasjg1"] += vitorias_jogador1
            resultado["vitoriasjg2"] += vitorias_jogador2
            resultado["pontosjg1"] += ponto1
            resultado["pontosjg2"] += ponto2
            if resultado["pontosjg1"] >= 3:
                resultado["vitoriasjg1"] += 1
                resultado["pontosjg1"] = 0
                resultado["pontosjg2"] = 0
            elif resultado["pontosjg2"] >= 3:
                resultado["vitoriasjg2"] += 1
                resultado["pontosjg1"] = 0
                resultado["pontosjg2"] = 0
            break

    if not encontrado:
        novo_resultado = {
            "nomejogo": "velha",
            "jogador1": jogador1,
            "jogador2": jogador2,
            "vitoriasjg1": vitorias_jogador1,
            "vitoriasjg2": vitorias_jogador2,
            "pontosjg1": ponto1,
            "pontosjg2": ponto2
        }
        lista_resultados.append(novo_resultado)

    with open("resultado.json", "w") as arquivo:
        json.dump(lista_resultados, arquivo)

def jogar_velha(jogador1, jogador2):
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    marca1 = "X"
    marca2 = "O"
    turno = 1
    vencedor = None
    mostrar_tabuleiro(tabuleiro)

    while vencedor is None:
        if turno == 1:
            print(f"Vez de {jogador1}. Escolha uma posição de 1 a 9, ou digite x para sair.")
            entrada = input()

            if entrada == "x":
                salvar_progresso(jogador1, jogador2, tabuleiro, turno, 0, 0)
                print("Jogo encerrado.")
                return None

            elif entrada in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                entrada = int(entrada)
                linha = (entrada - 1) // 3
                coluna = (entrada - 1) % 3

                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = marca1
                    mostrar_tabuleiro(tabuleiro)
                    vencedor = verificar_vencedor(tabuleiro)
                    turno = 2

                else:
                    print("Essa posição já está ocupada. Tente outra.")

            else:
                print("Entrada inválida. Digite um número de 1 a 9, ou x para sair.")

        elif turno == 2:
            print(f"Vez de {jogador2}. Escolha uma posição de 1 a 9, ou digite x para sair.")
            entrada = input()

            if entrada == "x":
                salvar_progresso(jogador1, jogador2, tabuleiro, turno, 0, 0)
                print("Jogo encerrado.")
                return None

            elif entrada in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                entrada = int(entrada)
                linha = (entrada - 1) // 3
                coluna = (entrada - 1) % 3

                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = marca2
                    mostrar_tabuleiro(tabuleiro)
                    vencedor = verificar_vencedor(tabuleiro)
                    turno = 1

                else:
                    print("Essa posição já está ocupada. Tente outra.")

            else:
                print("Entrada inválida. Digite um número de 1 a 9, ou x para sair.")

    if vencedor is not None:
        if vencedor == marca1:
            print(f"Parabéns, {jogador1}! Você ganhou!")
            atualizar_resultado(jogador1, jogador2, 1, 0, 1, 0)
            return jogador1

        elif vencedor == marca2:
            print(f"Parabéns, {jogador2}! Você ganhou!")
            atualizar_resultado(jogador1, jogador2, 0, 1, 0, 1)
            return jogador2

        elif vencedor == "empate":
            print("Empate! Ninguém ganhou.")
            return None

def iniciar_jogo():
    print("Bem-vindo ao jogo da velha!")
    print("Escolha uma opção:")
    print("1. Começar um jogo novo")
    print("2. Carregar o jogo anterior")
    print("x. Sair do jogo")

    opcao = input()

    while opcao != "x":
        if opcao == "1":
            print("Digite o nome do jogador 1:")
            jogador1 = input()
            print("Digite o nome do jogador 2:")
            jogador2 = input()
            pontos_jogador1 = 0
            pontos_jogador2 = 0

            while pontos_jogador1 < 3 and pontos_jogador2 < 3:
                vencedor = jogar_velha(jogador1, jogador2)

                if vencedor == jogador1:
                    pontos_jogador1 += 1
                elif vencedor == jogador2:
                    pontos_jogador2 += 1

                print(f"Pontos: {jogador1} - {pontos_jogador1}, {jogador2} - {pontos_jogador2}")

                if pontos_jogador1 < 3 and pontos_jogador2 < 3:
                    print("Quer jogar novamente? (s/n)")
                    resposta = input()

                    if resposta == "n":
                        salvar_progresso(jogador1, jogador2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], 1,
                                          pontos_jogador1, pontos_jogador2)
                        break
                    elif resposta == "x":
                        salvar_progresso(jogador1, jogador2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], 1,
                                          pontos_jogador1, pontos_jogador2)
                        print("Jogo encerrado.")
                        return None
                    elif resposta != "s":
                        print("Opção inválida. Digite s ou n, ou x para sair.")
                        resposta = input()

            print("Jogo encerrado.")
            return None

        elif opcao == "2":
            dados = carregar_progresso()
            jogador1 = dados["jogador1"]
            jogador2 = dados["jogador2"]
            pontos_jogador1 = dados["pontos_jogador1"]
            pontos_jogador2 = dados["pontos_jogador2"]

            while pontos_jogador1 < 3 and pontos_jogador2 < 3:
                vencedor = jogar_velha(jogador1, jogador2)

                if vencedor == jogador1:
                    pontos_jogador1 += 1
                elif vencedor == jogador2:
                    pontos_jogador2 += 1

                print(f"Pontos: {jogador1} - {pontos_jogador1}, {jogador2} - {pontos_jogador2}")

                if pontos_jogador1 < 3 and pontos_jogador2 < 3:
                    print("Quer jogar novamente? (s/n)")
                    resposta = input()

                    if resposta == "n":
                        salvar_progresso(jogador1, jogador2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], 1,
                                          pontos_jogador1, pontos_jogador2)
                        break
                    elif resposta == "x":
                        salvar_progresso(jogador1, jogador2, [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], 1,
                                          pontos_jogador1, pontos_jogador2)
                        print("Jogo encerrado.")
                        return None
                    elif resposta != "s":
                        print("Opção inválida. Digite s ou n, ou x para sair.")
                        resposta = input()

            print("Jogo encerrado.")
            return None

        else:
            print("Opção inválida. Digite 1 ou 2, ou x para sair.")
            opcao = input()

    print("Jogo encerrado.")
    return None

iniciar_jogo()
