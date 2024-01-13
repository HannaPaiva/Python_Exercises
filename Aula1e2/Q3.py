while True:
    #Valor para conversão
    print("************************************")
    print("        EUR  ==>  USD")
    print("************************************")

    try:
        valor_euro = float(input(''' Insira o valor, em euros, que deseja converter: '''))
        #Converte e mostra resultado SE o input for válido
        if type(valor_euro) == float or type(valor_euro) == int:
            taxa = 1.17
            valor_dolar = valor_euro * taxa
            print(valor_dolar)
            break
    except:
  
            print('Valor inválido. Tente novamente.')

   

