altura = float(input("Digite sua altura: "))

male = (72.7 * altura) - 58
famele = (62.1 * altura) - 44.7

formatMAle = "{:.2f}".format(male)
formatFamle = "{:.2f}".format(famele)

print(f"Peso ideal para sua altura \nHomem: {formatMAle}Kg \nMulher: {formatFamle}Kg")