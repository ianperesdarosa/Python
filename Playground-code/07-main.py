class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        if self.age < 18:
            print("Menor de idade cadastrado!")
        else: 
            print("Cadastro confiramdo!")
            print("Informações   ${self.name}, ")

put = Person("Pedro", 17)
put.myfunc()