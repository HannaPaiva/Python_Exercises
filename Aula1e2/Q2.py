import random
import math

def nums_aleatorios():
    ''' Função para escrever os números aleatórios, como pede a questão. '''
    a = random.randint(0, 10)  
    b = random.randint(5, 20)  
    c = random.randint(5, 20)  
    print(f"Os números aleatórios são: a = {a} b = {b} c = {c}")

    return a, b, c

def calcular_delta(a, b, c):
    '''Método que calcula o discriminante da função e devolve o valor de Delta'''
    delta = b**2 - 4*a*c
    return delta

def formula_resolvente(a, b, c, delta):
    ''' A formula que calcula a fórmula resolvente e mostra no ecrã o resultado '''
    if delta > 0 and a != 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes são: {raiz1} e {raiz2}")

    elif delta == 0 and a != 0:
        raiz = -b / (2*a)
        print(f"A raiz é: {raiz}")

    else:
        print("Não existem raízes reais.")

numeros = nums_aleatorios()
delta = calcular_delta(numeros[0], numeros[1], numeros[2])
formula_resolvente(numeros[0], numeros[1], numeros[2], delta)