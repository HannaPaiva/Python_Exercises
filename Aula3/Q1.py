''' 

Número primo = só é divisivel por 1 e por ele mesmo

'''
#função para achar divisores
def achar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def e_primo(divisores):
    if len(divisores) == 1 or len(divisores) == 2:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
divisores = achar_divisores(numero)
primo = e_primo(divisores)

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} é um número não primo.")
print(f"Divisores de {numero}: {divisores}")

