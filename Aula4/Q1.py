
a = []
cpar = 0
cimpar=0

for i in range(1,11):
    num = int(input(f"Insira o {i}º numero: "))
    a.append(num)


dif = max(a) - min(a)

for i in a:
    if (i % 2 == 0):
        cpar = cpar+1
    else:
        cimpar = cimpar+1

print(f"A diferença é {dif}")

print(f"São {cimpar} valores impar e {cpar} valores pares")
