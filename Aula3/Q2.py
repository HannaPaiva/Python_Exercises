#distancia entre 2 pontos
import math

x1 = float(input("Insira o primeiro ponto X: "))
x2 = float(input("Insira o segundo ponto X: "))

y1 = float(input("Insira o primeiro ponto Y: "))
y2 = float(input("Insira o segundo ponto Y: "))

distancia = math.sqrt(((x2 - x1)**2 + (y2-y1)**2))

print(f'A distância entre dois pontos é: {round(distancia, 3)}')
