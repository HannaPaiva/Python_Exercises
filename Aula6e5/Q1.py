
def receber_base_expoente():

    base = float(input("Digite a base para ser elevada a um número: "))

    expoente = float(input("O expoente: "))

    return base, expoente

def calcular_potencia(base, expoente):
    resultado = base**expoente
    return resultado


base, expoente = receber_base_expoente()

resultado = calcular_potencia(base, expoente)

print(f"O resultado é {resultado}")
