class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


kev = Person("Kevin Ntinyari")
print(f"{kev.name}")
kev.talk()

bob = Person("Bob Marley")
bob.talk()