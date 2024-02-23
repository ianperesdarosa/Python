f = int(input("Digite a temperatura em Fahrenheit: "))

convertC = (5 * (f-32)) / 9
formatedConvertC = "{:.2f}".format(convertC)

print(f"A temperatura em Fahrenheit convertida de Celsius é {formatedConvertC}°C")