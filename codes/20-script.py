import random

n1 = str(input("Digite o nome do primeiro aluno(a): "))
n2 = str(input("Digite o nome do segundo aluno(a): "))
n3 = str(input("Digite o nome do terceiro aluno(a): "))

array = [n1, n2, n3]

random.shuffle(array)

print(f"Aluno(a) sorteado foi: {array}")