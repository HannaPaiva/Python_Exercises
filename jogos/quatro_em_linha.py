def jogar_quatro_em_linha():
    linhas = 8
    colunas = 8

    tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]

    vez = "X"

    for _ in range(linhas * colunas):
        for row in tabuleiro:
            print("|".join(row))
        
        while True:
            try:
                escolha = int(input("Jogador " + vez + ", escolha uma coluna (1-" + str(colunas) + "): ")) - 1
                
                if not (0 <= escolha < colunas):
                    raise ValueError("Escolha fora do intervalo permitido.")
                
                for i in range(linhas - 1, -1, -1):
                    if tabuleiro[i][escolha] == " ":
                        tabuleiro[i][escolha] = vez
                        break
                else:
                    print("Essa coluna está cheia. Escolha outra.")
                    continue

                break  # Saia do loop se a escolha for válida

            except ValueError as e:
                print(f"Erro: {e}")
                continue

        # Verificar se há um vencedor (horizontalmente)
        for row in tabuleiro:
            if "XXXX" in "".join(row) or "OOOO" in "".join(row):
                for row in tabuleiro:
                    print("|".join(row))
                print("Jogador " + vez + " venceu!")
                return

        # Verificar se há um vencedor (verticalmente)
        for col in range(colunas):
            if "X" * 4 in "".join([tabuleiro[row][col] for row in range(linhas)]) or "O" * 4 in "".join([tabuleiro[row][col] for row in range(linhas)]):
                for row in tabuleiro:
                    print("|".join(row))
                print("Jogador " + vez + " venceu!")
                return

        if vez == "X":
            vez = "O"
        else:
            vez = "X"

    for row in tabuleiro:
        print("|".join(row))

    print("Empate!")

if __name__ == "__main__":
    jogar_quatro_em_linha()
