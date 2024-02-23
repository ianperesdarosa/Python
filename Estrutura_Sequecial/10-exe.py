c = int(input("Digite a temperatura em Celsius: "))
f = (c * 9/5) + 32

formatF = "{:.2f}".format(f)
print(f"A temperatura em Fahrenheit convertida de Celsius é {f}°F")