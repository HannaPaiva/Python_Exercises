import random
import json

# Palavras possíveis
palavras = ["cadeira", "mesa", "garrafa", "telefone", "biscoito", "mar"]

def carregar_jogo():
    try:
        with open("jogo_da_forca.json", "r") as arquivo:
            estado_jogo = json.load(arquivo)
        return estado_jogo
    except FileNotFoundError:
        return None

def salvar_jogo(letras_certas, tentativas, palavra_certa):
    estado_jogo = {
        "letras_certas": letras_certas,
        "tentativas": tentativas,
        "palavra_certa": palavra_certa
    }
    with open("jogo_da_forca.json", "w") as arquivo:
        json.dump(estado_jogo, arquivo)

def welcome():
    print("Bem-vindo ao jogo da forca! Vamos jogar!")

def escolher_letra():
    try:
        letra = input("Digite uma letra ou escreva ' . ' para fechar o jogo: ").lower()
        return letra[0]
    except IndexError:
        print("Erro na inserção. Tem certeza que inseriu uma letra?")

def verificar_letra(letra, letras_certas, palavra_certa, tentativas):
    if letra in letras_certas:
        print("Essa letra já foi inserida")
    elif letra in palavra_certa:
        print("A letra existe!")
        letras_certas.append(letra)
    else:
        tentativas += 1
        print(erros(tentativas))
        print(f"Letra não encontrada. Você pode errar mais {6 - tentativas} vezes ")
    return tentativas

def escrever_letra(palavra_certa, letras_certas):
    resultado = ""
    for letra in palavra_certa:
        if letra in letras_certas:
            resultado += letra
        else:
            resultado += "_"
    return resultado


def erros(tentativas):
    match tentativas:
        case 1:
              print(r'''   +---+
    |   |
    O   |
        |
        |
        |
        |
            ''')
        case 2: 
             print(r'''   +---+
    |   |
    O   |
    |   |
    |   |
        |
        |
            ''')
        case 3:
                print(r'''   +---+
    |   |
    O   |
    |\  |
    |   |
        |
        |
            ''')
        case 4:
                print(r'''   +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        |
            ''')
                
        case 5:
                print(r'''   +---+
    |   |
    O   |
   /|\  |
    |   |
     \  |
        |
            ''')
        case 6:
                print(r'''   +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        |
            ''')




# Variável para controlar se o usuário quer sair do jogo
sair = False

# Variável para controlar se o usuário quer um novo jogo ou continuar o anterior
novo_jogo = True

while not sair:
    if novo_jogo:
        # Escolher uma palavra aleatória
        index = random.randint(0, 5)
        palavra_certa = palavras[index]

        # Inicializar as variáveis
        letras_certas = []
        tentativas = 0
        venceu = False

        # Tentar carregar um jogo anterior
        estado_jogo_anterior = carregar_jogo()
        if estado_jogo_anterior:
            # Perguntar ao usuário se quer continuar o jogo anterior ou começar um novo
            opcao = input("Você tem um jogo salvo. Digite 1 para começar um novo jogo ou 2 para continuar: ")
            if opcao == "2":
                # Carregar as variáveis do jogo anterior
                letras_certas = estado_jogo_anterior["letras_certas"]
                tentativas = estado_jogo_anterior["tentativas"]
                palavra_certa = estado_jogo_anterior["palavra_certa"]

    welcome()
    # print(palavra_certa)
    palavra_transformada = escrever_letra(palavra_certa, letras_certas)
    print(palavra_transformada)

    while not sair and not venceu:
        resultado = ""
        if tentativas != 6:
            letra = escolher_letra()
            # Verificar se o usuário quer sair do jogo
            if letra == ".":
                sair = True
                break
            tentativas = verificar_letra(letra, letras_certas, palavra_certa, tentativas)
            resultado = escrever_letra(palavra_certa, letras_certas)
            print("Resultado: ", resultado)
            if resultado == palavra_certa:
                print("Parabéns! VENCEU!!")
                venceu = True
        else:
            print("OOOPPS! Você perdeu!")
            venceu = True

    # Salvar o estado atual do jogo
    salvar_jogo(letras_certas, tentativas, palavra_certa)
    print("Fim do jogo")
