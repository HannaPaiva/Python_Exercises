lista = []

qtd= int(input("Quantos elementos quer ter na lista?"))

for i in range(1, qtd+1):
    elementos = input("popule a lista com números ou palavras ")
    lista.append(elementos)

lista.sort()
print (f"A sua lista ordenada é {lista}")