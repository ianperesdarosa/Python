class Pessoa:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

p1 = Pessoa("Ian", 18, "Man")
print(p1.name)
print(p1.age)
print(p1.sex)