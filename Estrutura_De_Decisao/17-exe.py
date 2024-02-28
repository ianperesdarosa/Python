def bissexto(ano):
    if ano % 4 == 0:
        return "Ano e Bissexto!"
    else:
        return "Ano nao e Bissexto!"

print(bissexto(2023))