def tr(l1, l2, l3):
    
    if l1 == l2 == l3:
        return "Triângulo Equilátero"    
    elif l1 == l2 or l1 == l3 or l2 == l3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"


l1 = int(input("Digite o valor do l1 do Triângulo: "))
l2 = int(input("Digite o valor do l1 do Triângulo: "))
l3 = int(input("Digite o valor do l1 do Triângulo: "))

print(tr(l1, l2, l3))