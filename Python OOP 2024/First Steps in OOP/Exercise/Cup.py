class Cup:
    def __init__(self,size,quantity):
        self.size = size
        self.quantity = quantity

    def fill(self,quantity):
        ammount = self.quantity + quantity
        if ammount <= self.size:
            self.quantity = ammount
    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)

print(cup.status())

cup.fill(40)

cup.fill(20)

print(cup.status())