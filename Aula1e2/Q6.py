def inserir_dados():

    while True:
        try:
            print()
            largura = float(input("Digite a largura da forma: "))
            print()
            altura = float(input("Digite a altura da forma: "))
            print()
            break
        except:
            print("Digite um valor válido")


    return largura, altura


def verificar_forma(largura, altura):
    
    if largura == altura:
        forma = "quadrado"
    else:
        forma = "retângulo"

    return forma


def calcular_area(largura, altura):

    area = largura * altura

    return area



largura, altura = inserir_dados()
forma = verificar_forma(largura, altura)
area = calcular_area(largura, altura)

print()
print()
print(f"A área do {forma} é {area:.2f}")
print()
print()


