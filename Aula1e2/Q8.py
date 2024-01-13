from math import * 
while True:
    try:

        valor_1 = int(input("Insira o primeiro valor: "))
        valor_2 = int(input("Insira o segundo valor: "))
        valor_3 = int(input("Insira o terceiro valor: "))
        print(f"O valor máximo é {max(valor_1, valor_2, valor_3)}")

        break
    except:

        print("\nValor inserido é invalido. Tente novamente.\n")


