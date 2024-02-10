print('Digite as notas do Aluno(a)!')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

res = (nota1 + nota2 + nota3)

if res >= 18 :
    print(f'Nota: {res} \nAluno(a) aprovado!')
else:
    print(f'Nota: {res} \nAluno(a) reprovado!')