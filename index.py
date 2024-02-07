class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Index:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Subclasse: {cls.__name__}")


class MinhaSubclasse(Index, Person):
    pass

p1 = MinhaSubclasse(name="Alice", age=30)
print(f"Nome: {p1.name}, Idade: {p1.age}")