num = int(input("Insira um número para calcular: "))
fatorial = num
for i in range(1, num):
    fatorial = fatorial * i

print(f"O resultado fatorial é: {fatorial}")