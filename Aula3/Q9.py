
num_turmas = 3  

idade_mais_nova = 9999
idade_mais_velha = 0
raparigas = 0
nota_entrada_mais_alta = 0
genero_nota_entrada_mais_alta = None
turma_mais_nova = None
turma_mais_velha = None
turma_nota_entrada_mais_alta = None

for turma in range(1, num_turmas + 1):
    print(f"Turma {turma}:")
    num_alunos = int(input("Número de alunos: "))

    # Inicialize variáveis para acompanhar os resultados por turma
    turma_idade_mais_nova = 9999
    turma_idade_mais_velha = 0
    turma_raparigas = 0
    turma_nota_entrada_mais_alta = 0
    turma_genero_nota_entrada_mais_alta = None

    # Loop através dos alunos da turma
    for aluno in range(1, num_alunos + 1):
        idade = int(input("Idade do aluno: "))
        genero = int(input("Género (1 - Masculino, 0 - Feminino): "))
        nota_entrada = float(input("Nota de entrada: "))

        # Atualize os resultados da turma
        if idade < turma_idade_mais_nova:
            turma_idade_mais_nova = idade
        if idade > turma_idade_mais_velha:
            turma_idade_mais_velha = idade
        if genero == 0:
            turma_raparigas += 1
        if nota_entrada > turma_nota_entrada_mais_alta:
            turma_nota_entrada_mais_alta = nota_entrada
            turma_genero_nota_entrada_mais_alta = genero

    # Atualize os resultados globais
    if turma_idade_mais_nova < idade_mais_nova:
        idade_mais_nova = turma_idade_mais_nova
        turma_mais_nova = turma
    if turma_idade_mais_velha > idade_mais_velha:
        idade_mais_velha = turma_idade_mais_velha
        turma_mais_velha = turma
    raparigas += turma_raparigas
    if turma_nota_entrada_mais_alta > nota_entrada_mais_alta:
        nota_entrada_mais_alta = turma_nota_entrada_mais_alta
        genero_nota_entrada_mais_alta = turma_genero_nota_entrada_mais_alta
        turma_nota_entrada_mais_alta = turma

# Apresente os resultados globais
print(f"\n A turma com o aluno mais novo é a Turma {turma_mais_nova}.")
print(f" A turma com o aluno mais velho é a Turma {turma_mais_velha}.")
print(f"O número de raparigas é {raparigas}.")
print(f"A turma com o aluno com a nota de entrada mais alta é a Turma {turma_nota_entrada_mais_alta}.")
print(f" A nota de entrada mais alta foi {nota_entrada_mais_alta} e o género da pessoa que teve essa nota é {'Masculino' if genero_nota_entrada_mais_alta == 1 else 'Feminino'}.")
