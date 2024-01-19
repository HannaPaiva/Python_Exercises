import json
import velha as velha


def exibir_menu():
    print("\nMenu de Jogos:")
    print("1. Jogo da Velha")
    print("2. 4 em Linha")
    print("3. Batalha Naval")
    print("4. Forca")
    print("5. Campo Minado")
    print("6. Glória")
    print("10. Visualizar Histórico de Jogos")
    print("x. Sair")

def jogo_da_velha():
    return velha.jogo_velha()

def salvar_relatorio(relatorio):
    try:
        with open("relatorio.json", "r") as arquivo:
            dados_antigos = json.load(arquivo)
    except FileNotFoundError:
        dados_antigos = []

    dados_antigos.append(relatorio)

    with open("relatorio.json", "w") as arquivo:
        json.dump(dados_antigos, arquivo, indent=2)

def visualizar_historico():
    try:
        with open("relatorio.json", "r") as arquivo:
            historico = json.load(arquivo)
            for jogo in historico:
                print(json.dumps(jogo, indent=2))
    except FileNotFoundError:
        print("Nenhum histórico disponível.")

if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_velha = jogo_da_velha()
            salvar_relatorio(relatorio_velha)
        elif opcao == "10":
            visualizar_historico()
        elif opcao.lower() == "x":
            break
        else:
            print("Opção inválida. Tente novamente.")
