print("Matutino \nVespertino \nNoturno")

turno = str(input("Insira o turno que você trabalha: "))

if turno.upper() == "M": 
    print("Bom Dia !")
    
elif turno.upper() == "V":
    print("Boa Tarde!")

elif turno.upper() == "N":
    print("Boa Noite!")