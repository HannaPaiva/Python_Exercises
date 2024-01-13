def procurar(input):
    vetor = [1, 2, 3, 4]
    resultado = False
    if(input in vetor):
        resultado = True
        print("True. Existe esse número no vetor")
    else:
        resultado = False
        print("False. Não existe esse número no vetor")

    return resultado

variavel = int((input("Escreva o número que deseja procurar no vetor")))
resultado = procurar(variavel)        
print(resultado)