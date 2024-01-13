while True:
    valor_inicial = int(input("Digite um número para ser o valor inicial:  "))
    valor_final = int(input("Digite um número para ser o valor final:  "))
    soma = 0

    if valor_final <= valor_inicial:
            print("introduza uma diferença correta. Esse intervalo está invertido")
            continue
    else:
        for i in range(valor_inicial, valor_final + 1):
            soma = soma + i
    
    print(f"Valor da soma de {valor_inicial} até {valor_final} é {soma}")   
    break  

    