mensagem = ''

while True:

    print("L/l para ligar")
    print("D/d para desligar")
    print("F/f para furar")
    mensagem = input("Diga o que a máquina vai fazer: ")

    print()
    if mensagem.lower() == "d":
        print()
        print("desligar...")
        print()
        break

    elif mensagem.lower() == "l":
        instrucao = 'ligar'
        print()
        print("Instrução recebida:", instrucao)
        print()

    elif mensagem.lower() == 'f':
        instrucao = 'furar'
        print()
        print("Instrução recebida:", instrucao)
        print()
    else: print('insira um comando válido')


