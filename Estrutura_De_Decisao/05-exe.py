def aluno_Nota(n1, n2, n3):
    notas = n1 + n2 + n3

    if notas >= 18:
        return "Aluno(a) Aprovado!"
    if notas == 30:
        return "Aluno(a) Aprovado com Dinstinção!"
    else:
        return "Aluno(a) Reprovado!"
    
n1 = int(input("Nota: "))
n2 = int(input("Nota: "))
n3 = int(input("Nota: "))

print(aluno_Nota(n1, n2, n3))