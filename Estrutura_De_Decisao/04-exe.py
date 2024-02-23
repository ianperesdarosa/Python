def verificar_letra(caractere):
    vogais = 'aeiouAEIOU'
    
    if caractere.isalpha() and len(caractere) == 1:
        if caractere in vogais:
            return f'{caractere} é uma vogal.'
        else:
            return f'{caractere} é uma consoante.'
    else:
        return 'Por favor, digite apenas uma letra.'

letra = input("Digite uma letra: ")

resultado = verificar_letra(letra)

print(resultado)
