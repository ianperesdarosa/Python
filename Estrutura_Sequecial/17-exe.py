import math

# Definindo os valores
area_a_pintar = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calculando a quantidade de tinta necessária em litros
litros_de_tinta = area_a_pintar / 6

# Adicionando 10% de folga
litros_de_tinta_com_folga = litros_de_tinta * 1.1

# Calculando o número de latas necessárias
latas_de_tinta = math.ceil(litros_de_tinta_com_folga / 18)

# Calculando o número de galões necessários
galoes_de_tinta = math.ceil(litros_de_tinta_com_folga / 3.6)

# Calculando os preços para cada situação
preco_latas = latas_de_tinta * 80
preco_galoes = galoes_de_tinta * 25

# Misturando latas e galões para minimizar o desperdício
latas_para_misturar = int(litros_de_tinta_com_folga // 18)
litros_restantes = litros_de_tinta_com_folga % 18
galoes_para_misturar = math.ceil(litros_restantes / 3.6)

# Calculando o preço para a mistura de latas e galões
preco_mistura = (latas_para_misturar * 80) + (galoes_para_misturar * 25)

# Exibindo os resultados
print("Para pintar", area_a_pintar, "metros quadrados:")
print("Comprando apenas latas de 18 litros, você precisará de", latas_de_tinta, "latas e o preço total é R$", preco_latas)
print("Comprando apenas galões de 3,6 litros, você precisará de", galoes_de_tinta, "galões e o preço total é R$", preco_galoes)
print("Misturando latas e galões, você precisará de", latas_para_misturar, "latas e", galoes_para_misturar, "galões, e o preço total é R$", preco_mistura)