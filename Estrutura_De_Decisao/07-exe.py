def maiorQ(value1, value2, value3):
    maior = max(value1, value2, value3)
    menor = min(value1, value2, value3)
    
    return f"Maior valor: {maior}\nMenor valor: {menor}"
    
value1 = int(input("Digite um número: "))
value2 = int(input("Digite um número: "))
value3 = int(input("Digite um número: "))

print(maiorQ(value1, value2, value3))