def receber_num():

    try:
        num = int(input("Insira um número: "))
    except:
        print("Isto não é um número válido")

    return num

def devolver_menor(num):
    min = 0 
    while True:
        if(num != 0):
            unidades = num % 10
            num = num//10
            if (unidades < min):
                min = unidades
            print(num) 
        else: break

    return min


num = receber_num()
menor = devolver_menor(num)


print (f"O menor número é:{menor} ")

