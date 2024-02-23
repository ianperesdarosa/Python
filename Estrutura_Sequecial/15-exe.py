soldo = float(input("Digite seu sálario: "))
formatSoldo = "{:.2f}".format(soldo)

inss = 8
impRenda = 11
sindicato = 5

descontoInss = (soldo / 100) * inss
descontoImpoRenda = (soldo / 100) * impRenda
descontoSindicato = (soldo / 100) * sindicato

dInss = soldo - descontoInss
dImpRenda = soldo - descontoImpoRenda
dSindicato = soldo - descontoSindicato

valorTotal = (descontoInss + descontoImpoRenda + descontoSindicato) - soldo

formatDescontoInss = "{:.2f}".format(descontoInss)
formatDescontoImpoRenda = "{:.2f}".format(descontoImpoRenda)
formatDescontoSindicato = "{:.2f}".format(descontoSindicato)
formatValorTotal = "{:.2f}".format(valorTotal * -1)

print(f"Sálario liquido: R${formatSoldo} \nSálario com descontado: R${formatValorTotal}")
print(f"////Descontos//// \nINSS: R${formatDescontoInss} \nImposto de Renda: R${formatDescontoImpoRenda} \nSindicato: R${formatDescontoSindicato}")