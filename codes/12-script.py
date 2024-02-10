v = float(input('Digite o valor do produto R$:'))
d = int(input('Digite o o desconto que sera aplicado a compra do produto: '))
desconto = (d / 100) * v
novoPreco = v - desconto

print(f'Valor do produto: R${v} \nDesconto: {d}% \nValor do produto com desoconto: R${novoPreco}')



