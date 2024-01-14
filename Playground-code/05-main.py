class Pessoa:
    def __init__(self, name, age, date):
        self.name = name
        self.age = age
        self.date = date

    def my_Func(self):
        return f"{self.name}, {self.age}, {self.date}"      

p1 = Pessoa('Ian', 19, '08/08/2004')

print(p1.my_Func())