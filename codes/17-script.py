import math

catetoOp = float(input("Digite o Cateto Oposto do triângulo: "))
catetoAd = float(input("Digite o Cateto Adjacente do triângulo: "))

potCateOp = math.pow(catetoOp  ,2)
potCateAd = math.pow(catetoAd, 2)

hipo = catetoAd + catetoOp

res = math.sqrt(hipo)
fRes = "{:.2f}".format(res)

print(f"O comprimento da Hipotenusa é: {fRes}")