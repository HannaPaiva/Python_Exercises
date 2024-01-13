alunos_deloitte = {
"Hanna": {"idade": 20, "altura": 1.69},
"Francisco": {"idade": 35, "altura": 1.71},
"Adriano": {"idade": 20, "altura": 1.80},
"Afonso": {"idade": 19, "altura": 1.85},
"Afonso": {"idade": 19, "altura": 1.97},
"Lucas": {"idade": 18, "altura": 1.75},

}

soma_alturas = 0
idade_aluno_mais_novo = 9999
nome_aluno_mais_novo = None
altura_aluno_mais_alto = 0
nome_aluno_mais_alto = None



for nome, dados in alunos_deloitte.items():
    
    altura = dados["altura"]
    idade = dados["idade"]
    
    soma_alturas += altura
    
    if idade < idade_aluno_mais_novo:
        idade_aluno_mais_novo = idade
        nome_aluno_mais_novo = nome

    if altura > altura_aluno_mais_alto:
        altura_aluno_mais_alto = altura
        nome_aluno_mais_alto = nome    




# Calcula a média das alturas
media_alturas = soma_alturas / len(alunos_deloitte)

# Imprime a média das alturas e o aluno mais novo
print(f"A média das alturas dos alunos é: {media_alturas:.2f} metros")
print(f"O(a) aluno(a) mais novo(a) é {nome_aluno_mais_novo} com {idade_aluno_mais_novo} anos.")
print(f"O(a) aluno(a) mais alto(a) é {nome_aluno_mais_alto} com {altura_aluno_mais_alto} de altura.")