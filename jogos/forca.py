import random
#Palavras possíveis
palavras = ["cadeira", "mesa", "garrafa", "telefone", "biscoito", "mar"]

index = random.randint(0,5)
letras_certas = []

tentativas = 0
venceu = False
palavra_certa = palavras[index]

def welcome():
    
    print()
    print()
    print()
    print("Bem-vindo ao jogo da forca! Vamos jogar!")
    print()
    # print("Esta é a palavra: ")

def transformar_em_underscores(palavra):
    '''função que retorna o tamanho da string em underscores'''
    palavra_transformada = "_"* len(palavra)
    return palavra_transformada

def escolher_letra():
    '''Função de input. '''
    while True:
        try:
            letra = input("Digite uma letra: ").lower()
            if letra and letra.isalpha():  # Verifica se o input não está vazio e é uma letra
                return letra[0]
            else:
                print("Por favor, insira uma letra válida.")
        except IndexError:
            print("Erro na inserção. Tem certeza que inseriu uma letra?")



def verificar_letra(letra, letras_certas, palavra_certa, tentativas):
        
    if letra in letras_certas:
            print("Essa letra já foi inserida")

    elif letra in palavra_certa:
            print("A letra existe!")
            letras_certas.append(letra)
        
    if letra not in palavra_certa:
            tentativas = tentativas + 1
            print(erros(tentativas))
            chances = 6-tentativas
            if chances < 1:
                print(f"Letra não encontrada. Você pode errar mais {chances} vezes ")
            else:
                print(f"Letra não encontrada. Você pode errar mais {chances} vez ")
    return tentativas
        


def escrever_letra(palavra_certa, letras_certas):
     
     escrever = ""
     for letra in palavra_certa:
          if letra in letras_certas:
               escrever = escrever+ letra
          else:
               escrever = escrever + "_"

     return escrever


def erros(tentativas):
    match tentativas:
        case 1:
              print(r'''  +---+
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





welcome()

print(palavra_certa)

palavra_transformada = transformar_em_underscores(palavra_certa)

print(palavra_transformada)


while True:
    
   
    resultado = ""
    if tentativas != 6:
        letra = escolher_letra()
        tentativas = verificar_letra(letra, letras_certas, palavra_certa, tentativas)
        resultado = escrever_letra(palavra_certa, letras_certas)
        print ("Resultado: ", resultado)
        if resultado == palavra_certa:
             print("Parabéns! WIN WIN AND HIS NAME IS JHOON CENAAA PAMPAMRAMPAM")
             break
    
    else:
         print("Perdeu! Você perdeu! IHIHIHI")
         break
    

print("Fim do jogo")