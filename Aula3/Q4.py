numero = int(input("Digite um número para a tabuada: "))

tabuada_max = 10

# Loop para gerar a 
print("**********************************")
print()
print(f"Tabuada do {numero}:")
for i in range(0, tabuada_max + 1):
    produto = numero * i
    print(f"{numero} x {i} = {produto}")

print()
print("**********************************")