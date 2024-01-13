lista = []

qtd= int(input("Quantos elementos quer ter na lista? "))

for i in range(1, qtd+1):
    elementos = input("popule a lista com números ou palavras ")
    lista.append(elementos)

print (f"A sua lista ordenada é {lista}")

pesquisar = input("Digite o valor que deseja pesquisar: ")

lista.index(pesquisar)

print(f"o valor {pesquisar} está na posição {lista.index(pesquisar) + 1} ")