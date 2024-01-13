while True:

    try:

        valor = float(input("Insira o valor da nota do aluno: "))

        if valor >=9.5:
            print(f'O aluno tirou {valor}, significa que foi aprovado')

        elif valor <9.5:
            print(f'O aluno tirou {valor}, reprovado')

        elif valor < 0 and valor > 20:
            print("insira uma nota válida")

        break
    except:
        print('Insira uma nota válida')             