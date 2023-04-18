print("Vamos descobrirmos se o número e Par ou Ímpar?")

value = input("Digite o número:")
process = int(value)

if (process % 2) == 0:
    print(value, "é um número Par..")
else:
    print(value, "é um número Ímpar..")