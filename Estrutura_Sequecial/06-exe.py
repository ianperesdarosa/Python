import  math

d = float(input("Digite o diâmetro do círculo: "))

raio = d / 2
pi = math.pi

resRaio = pow(raio, 2)

fRaio = pi * resRaio

formated = "{:.2f}".format(fRaio)

print(f"Resultado: {formated}metros quadrados.")

