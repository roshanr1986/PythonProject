class iceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients=ingredients
        self.toppings=toppings
        print(self.ingredients)
        print(self.toppings)

    def scoops(self):
        res=[]
        for x in self.ingredients:
            for y in self.toppings:
                res.append([x,y])
        return res


machine = iceCreamMachine(["Vanila", "Chocolate"],["Strawbery sause"])
print(machine.scoops())

