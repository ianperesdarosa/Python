car = input("Digite a marca e modelo do seu carro alugado: ")
algDay = int(input("Digite a quantidade de dias que o carro foi alugado: "))
kmR = float(input("Digite quantos kilometros foi rodado com o carro alugado: "))

calcDay = 60 * algDay
calcKmR = 0.15 * kmR
calcRes = calcKmR + calcDay
formatRes = "{:.2f}".format(calcRes)

print(f"Marca e modelo do carro: {car} \nDias alugados: {algDay} \nKilometros rodados: {kmR} \nvalor a ser pago do aluguel: R${formatRes}")