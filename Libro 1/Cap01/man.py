class Man:
    def __init__(self, name):
        self.name = name
        print("Iniciado!")

    def hello(self):
        print("Hola " + self.name + "!")

    def goodbye(self):
        print("Adios " + self.name + "!")

m = Man("Irving")
m.hello()
m.goodbye()
