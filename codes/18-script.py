import math

angulo = float(input("Digite o Angulo que você deseja: "))

seno = math.sin(math.radians(angulo))
fSeno = "{:.2f}".format(seno)
print(f"O ângulo de {angulo} tem o Seno de {fSeno}!")

cosse = math.cos(math.radians(angulo))
fCosse = "{:.2f}".format(cosse)
print(f"O ângulo de {angulo} tem o Cosseno de {fCosse}!")

tan = math.tan(math.radians(angulo))
fTan = "{:.2f}".format(tan)
print(f"O ângulo de {angulo} tem a Tangente de {fTan}!")