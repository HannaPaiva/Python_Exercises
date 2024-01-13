def inserir_nome():
    nome_completo = input("Insira o seu nome completo: ")
    return nome_completo


def separar_nome(nome_completo):

    nome_separado = nome_completo.split(" ")
    return nome_separado

def reordenar_nome(nome_separado):
   
    final = nome_separado[-1] + ", " +  " ".join(nome_separado[0:-1])
    return final


nome = inserir_nome()
nome_separado = separar_nome(nome)
nome_reordenado = reordenar_nome(nome_separado)

print("Seu nome reordenado é: ", nome_reordenado)