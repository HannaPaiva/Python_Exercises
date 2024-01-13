
pares = []
impares= []

def nums():

    vetor = []
    for nums in range(1,11):
        numeros = int(input(f"Escreva 10 números inteiros. Escreva o {nums}º numero: "))
        vetor.append(numeros)

    return vetor


def diferenca(vetor):
    diferenca = max(vetor) - min(vetor)
    return diferenca


def pares_impares(vetor):
    
    for posicoes in vetor:
        if (posicoes % 2 == 0 ):
            pares.append(posicoes)
        else:
            impares.append(posicoes)
        
    return pares, impares


numeros = nums()
diferentes = diferenca(numeros)
quantos = pares_impares(numeros)

print("Os números são: ", numeros)
print("A diferença entre o maior e o menor é: ", diferentes)
print(f"os pares são: {quantos[0]} e são {len(quantos[0])} ")
print(f"os ímpares são: {quantos[1]} e são {len(quantos[1])} ")