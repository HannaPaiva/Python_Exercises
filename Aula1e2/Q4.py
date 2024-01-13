
import math

while True:
    try:
        raio = float(input("Digite o raio da circunferência: "))

        perimetro = 2* math.pi * raio

        area = math.pi * (raio**2)

        break
    except:
        print("\n O valor do raio não é válido! \n")


print(f"O perimetro da circunferência, com raio {raio}, tem a área de {round(area, 3)} e perímetro {round(perimetro, 3)}")

