value = str(input("Digite seu nome completo: "))

lowerCase = value.lower()
upperCase = value.upper()

formatStrip = value.replace(" ", "")
count = len(formatStrip)

fNameN = value.find(" ")

print("Analisando seu nome!")
print(f"Seu nome em maiúsculas: {upperCase}")
print(f"Seu nome em minúsculas: {lowerCase}")
print(f"Seu nome tem ao todo {count} de letras")
print(f"Seu primeiro nome tem {fNameN} letras")