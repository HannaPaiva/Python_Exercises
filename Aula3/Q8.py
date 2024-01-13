def fatoracao_primos(numero):
    fatores = []
    divisor = 2
    #https://www.todamateria.com.br/decomposicao-em-fatores-primos/#:~:text=Um%20m%C3%A9todo%20simples%20para%20decompor,at%C3%A9%20o%20resto%20ser%201.
    while divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero // divisor
            print(f"Resto {numero}")
        else:
            divisor += 1
    
    return fatores


numero = int(input("Digite um número inteiro para calcular sua fatoração em números primos: "))

if numero <= 1:
    print("A fatoração não é possível para números menores ou iguais a 1.")
else:
    fatores = fatoracao_primos(numero)
    fatores_str = ' x '.join([str(fator) for fator in fatores])
    # fatores_str = ' x '.join(map(str, fatores))

    print(f"A fatoração de {numero} em números primos é: {fatores_str}")

fatoracao_primos(100)

