import math

class Bask:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def equa(self):
        xB = pow(self.b, 2)
        delta = xB - (4 * self.a * self.c)

        if delta < 0:
            return "A equação não possui raízes reais"

        else:
            calc2FasePositivo = (-self.b + math.sqrt(delta)) / (self.c * 2)

            calc2FaseNegativo = (-self.b - math.sqrt(delta)) / (self.c * 2)

            s = calc2FasePositivo, calc2FaseNegativo

            return s
        
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
        
app = Bask(a, b, c)
res = app.equa()

print(res)
