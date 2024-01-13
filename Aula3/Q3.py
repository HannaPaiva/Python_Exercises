def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if 0 <= media <= 20:
        if media >= 9.5:
            return "Aprovado"
        else:
            return "Reprovado"
    else:
        return "Nota fora do intervalo válido (0-20)"


notas = []
disciplinas = ["Matemática", "Português", "Inglês", "Geografia"]


for disciplina in disciplinas:
    nota = float(input(f"Digite a nota de {disciplina}: "))
    while nota < 0 or nota > 20:
        print("Nota fora do intervalo válido (0-20). Tente novamente.")
        nota = float(input(f"Digite a nota de {disciplina}: "))
    notas.append(nota)


media = calcular_media(notas)

resultado = verificar_aprovacao(media)

print(f"A média do aluno é {media:.2f}. Ele está {resultado}.")