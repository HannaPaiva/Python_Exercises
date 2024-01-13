linhas = 8
colunas = 8

tabuleiro = [[" " for _ in range(colunas)] for _ in range(linhas)]

vez = "X"

for _ in range(linhas * colunas):
    for row in tabuleiro:
        print("|".join(row))
    
    escolha = int(input("Jogador " + vez + ", escolha uma coluna (1-" + str(colunas) + "): ")) - 1
    
    for i in range(linhas - 1, -1, -1):
        if tabuleiro[i][escolha] == " ":
            tabuleiro[i][escolha] = vez
            break
    else:
        print("Essa coluna está cheia. Escolha outra.")
        continue
    
    # Verificar se há um vencedor (horizontalmente)
    for row in tabuleiro:
        if "XXXX" in "".join(row) or "OOOO" in "".join(row):
            for row in tabuleiro:
                print("|".join(row))
            print("Jogador " + vez + " venceu!")
            exit()
    
    # Verificar se há um vencedor (verticalmente)
    for col in range(colunas):
        if "X" * 4 in "".join([tabuleiro[row][col] for row in range(linhas)]) or "O" * 4 in "".join([tabuleiro[row][col] for row in range(linhas)]):
            for row in tabuleiro:
                print("|".join(row))
            print("Jogador " + vez + " venceu!")
            exit()
    
    if vez == "X":
        vez = "O"
    else:
        vez = "X"

for row in tabuleiro:
    print("|".join(row))

print("Empate!")
