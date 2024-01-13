def receber_num():

    try:
        num = int(input("Insira um número: "))
    except:
        print("Isto não é um número válido")

    return num

def devolver_maior(num):
    max = 0 
    while True:
        if(num != 0):
            unidades = num % 10
            num = num//10
            if (unidades > max):
                max = unidades
            print(num) 
        else: break

    return max


num = receber_num()
maior = devolver_maior(num)


print (f"O maior número é:{maior} ")

