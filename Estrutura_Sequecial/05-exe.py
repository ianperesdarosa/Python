print("Conversor de Metros para Centémetros")

valueM = int(input("Digite o valor em Metros: "))
valueC = int(input("Digite o valor em  Centémetros: "))

convertC = valueM * 100
convertM = valueC / 100

formatRes = "{:.2f}".format(convertM)

print(f"O valor convertido: {convertC}cm")
print(f"O valor convertido: {formatRes}m")