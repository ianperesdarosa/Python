"""
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
"""

#New version!!
class Salario:
    def __init__(self, salario):
        self.salario = salario
        self.inss = 8
        self.imp_renda = 11
        self.sindicato = 5

    def calcular_desconto(self, porcentagem):
        return (self.salario / 100) * porcentagem

    def calcular_salario_liquido(self):
        desconto_inss = self.calcular_desconto(self.inss)
        desconto_imposto_renda = self.calcular_desconto(self.imp_renda)
        desconto_sindicato = self.calcular_desconto(self.sindicato)

        # Calculando o total de descontos
        total_descontos = desconto_inss + desconto_imposto_renda + desconto_sindicato
        salario_liquido = self.salario - total_descontos

        return salario_liquido, desconto_inss, desconto_imposto_renda, desconto_sindicato

    def exibir_relatorio(self):
        salario_liquido, desconto_inss, desconto_imposto_renda, desconto_sindicato = self.calcular_salario_liquido()

        print(f"Salário Bruto: R${self.salario:.2f}")
        print(f"Salário Líquido: R${salario_liquido:.2f}")
        print("////Descontos////")
        print(f"INSS: R${desconto_inss:.2f}")
        print(f"Imposto de Renda: R${desconto_imposto_renda:.2f}")
        print(f"Sindicato: R${desconto_sindicato:.2f}")
        print(f"Total de Descontos: R${(self.salario - salario_liquido):.2f}")


# Função principal para execução
def main():
    try:
        salario = float(input("Digite seu salário: "))
        calculo_salario = Salario(salario)
        calculo_salario.exibir_relatorio()
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# Executa o programa
if __name__ == "__main__":
    main()
