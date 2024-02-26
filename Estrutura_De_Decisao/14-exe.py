def notas(n1, n2, n3):
    validator = (n1 + n2 + n3) / 3

    if 0 <= validator < 4:
        return "Nota: E \nReprovado!"
    elif 4 <= validator < 6:
        return "Nota: D \nReprovado!"
    elif 6 <= validator < 7.5:
        return "Nota: C \nAprovado!"
    elif 7.5 <= validator < 9:   
        return "Nota: B \nAprovado!"
    elif 9 <= validator <= 10:
        return "Nota: A \nAprovado!"
    else: 
        return "Error!"

n1 = float(input("Digite a nota do 1 Trimestre: "))
n2 = float(input("Digite a nota do 2 Trimestre: "))
n3 = float(input("Digite a nota do 3 Trimestre: "))

print(notas(n1, n2, n3))