notas_disciplinas = []

while True:
    disciplina = input("Insira o nome da disciplina: ")

    if disciplina.lower() == "x":
        break

    try:
        nota = float(input("Insira a nota: "))
        palavras = disciplina.split()
        iniciais = ""  
        for palavra in palavras:
            iniciais += palavra[0]

        notas_disciplinas.append({"disciplina": iniciais, "nota": nota})

    except ValueError:
        print("Um erro aconteceu, insira uma nota válida")

for item in notas_disciplinas:
    print(item["disciplina"] + " ---------> " + str(item["nota"]))
