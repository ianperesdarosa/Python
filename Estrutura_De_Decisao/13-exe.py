def weekN(value):
    
    if value == 1:
        return "Segunda-Feira!"
    elif value == 2:
        return "Terça-Feira!"
    elif value == 3:
        return "Quarta-Feira!"
    elif value == 4: 
        return "Quinta-Feira"
    elif value == 5:
        return "Sexta-Feira!"
    elif value == 6:
        return "Sábado"
    elif value == 7:
        return "Domingo!"
    else: 
        return "Error! Error!"
    
value = int(input('Digite o valor corespondendo a semana: '))
print(weekN(value))