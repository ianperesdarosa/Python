horas = int(input("Digite quantas horas você trabalha: "))
quantHroas = int(input("Digite o valor de quantidade de horas aculadas: "))

valorHora = horas * quantHroas

if valorHora <= 900: 
    print("Isento!")

elif valorHora >= 1500:
    ir = (5 / 100) * valorHora
    resIr = ir - valorHora
    print(f"IR: R${resIr - valorHora}")

    inss = (10 / 100) * valorHora
    resInss = inss - valorHora
    print(f"INSS: R${resInss - valorHora}")

elif valorHora >= 1500:
    ir = (10 / 100) * valorHora
    resIr = ir - valorHora
    print(f"IR: R${resIr - valorHora}")

    inss = (20 / 100) * valorHora
    resInss = inss - valorHora
    print(f"INSS: R${resInss - valorHora}")