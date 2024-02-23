print("digite suas notas!")

n1 = float(input("Digite o nota1: "))
n2 = float(input("Digite o nota2: "))
n3 = float(input("Digite o nota3: "))
n4 = float(input("Digite o nota4: "))

soma = n1 + n2 + n3 + n4

if soma >= 24:
    print("Aluno(a) aprovado!")

else:
    print("Aluno(a) Reprovado!")