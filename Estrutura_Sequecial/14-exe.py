fish = int(input("Digite o peso dos peixes: "))

valueFish = 4

if fish > 50:
    print(f"Taxa: R${(fish - 50) * 4}")
else:
    print(f"Taxa não aplicada!")