print("Bem vinda a Calculadora PyTerminal79x!")

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

print("1 = Soma")
print("2 = Subtração")
print("3 = Multiplicação")
print("4 = Divisão")
print("5 = Sair")

operation = int(input("Escolha da operação: "))

if operation == 1:
    res = (n1 + n2)
    print(res)   
elif operation == 2:
    res = (n1 - n2)
    print(res) 
elif operation == 3:
    res = (n1 * n2)
    print(res) 
elif operation == 4:
    res = (n1 / n2)
    print(res) 
elif operation == 5:
    print("Exit!")
else:
    print("Error!")