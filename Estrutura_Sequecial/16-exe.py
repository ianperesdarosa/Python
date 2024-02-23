import math

# Definindo os valores
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária em litros
litros_de_tinta = area_a_pintar / 3

# Calculando o número de latas necessárias
latas_de_tinta = math.ceil(litros_de_tinta / 18)

# Calculando o preço total
preco_total = latas_de_tinta * 80

# Exibindo os resultados
print("Você precisará de", latas_de_tinta, "latas de tinta.")
print("O preço total é R$", preco_total)