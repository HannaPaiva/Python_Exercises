alunos = {}
contador = 0
idade_mais_novo = 999
nome_mais_novo = " "
cc_mais_novo = " "

while True:

    contador = contador + 1 
    nome = input(f"Insira o nome do aluno número {contador}. (Quando o nome ou idade forem 999 o programa vai ser encerrado):  ")
   
    if nome == "999" :
        print('Encerrando o programa...')

        for aluno, dados in alunos.items():
          _idade = dados["idade"]
          _cc = dados["cc"]
          if _idade < idade_mais_novo:
            idade_mais_novo = _idade
            cc_mais_novo = _cc
            nome_mais_novo = aluno
        break

    else:
        idade = int(input(f"Insira a idade do aluno número {contador}: "))
        if idade == 999: 
           break
        else:
            cc = input(f"Insira o número do cartão de cidadao do aluno número {contador} ")
            novo_aluno = {"idade": idade, "cc": cc}
            alunos[nome] = novo_aluno

print(f"O nome da pessoa mais nova é: {nome_mais_novo} com {idade_mais_novo} anos")