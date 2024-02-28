def aluno(n1, n2, n3):
    count = (n1 + n2 + n3) / 3

    if count >= 7:
        return "Aluno(a) Aprovado!"
    elif count == 10:
        return "Aluno(a) Aprovado com priacao!"
    elif count < 7:
        return "Aluno(a) Reprovado!"
    
n1 = int(input("Digite a nota: "))
n2 = int(input("Digite a nota: "))
n3 = int(input("Digite a nota: "))

notasAluno = aluno(n1, n2, n3)

print(notasAluno)