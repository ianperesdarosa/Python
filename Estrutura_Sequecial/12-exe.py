altura = float(input("Digite sua altura: "))
calc = (72.7 * altura) - 58

formatCalc = "{:.2f}".format(calc)

print(f"Seu o pesso ideal para sua altura é: {formatCalc}")