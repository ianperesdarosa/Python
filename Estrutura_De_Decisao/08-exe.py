print("Digite o preço de três produtos")

product01 = float(input("Digite o preço do produto: R$"))
product02 = float(input("Digite o preço do produto: R$"))
product03 = float(input("Digite o preço do produto: R$"))

select = min(product01, product02, product03)

print(f"O melhor escolha de preço é o produto de R${select}")