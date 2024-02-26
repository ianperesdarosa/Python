soldo = float(input("Digite seu sálario: "))

if soldo >= 280:
    bonefication = (20 / 100) * soldo
    newSoldo = bonefication + soldo

    print(f"Reajuste de sálario que era de R${soldo} foi para R${newSoldo}") 

elif soldo >= 280 or soldo <= 700:
    bonefication = (15 / 100) * soldo
    newSoldo = bonefication + soldo

    print(f"Reajuste de sálario que era de R${soldo} foi para R${newSoldo}")

elif soldo >= 700 or soldo <= 1500:
    bonefication = (10 / 100) * soldo
    newSoldo = bonefication + soldo
    print(f"Reajuste de sálario que era de R${soldo} foi para R${newSoldo}")

elif soldo > 1500:
    bonefication = (5 / 100) * soldo
    newSoldo = bonefication + soldo
    
    print(f"Reajuste de sálario que era de R${soldo} foi para R${newSoldo}")