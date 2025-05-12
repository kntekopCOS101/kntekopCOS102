# Another example using SELF

class car():

    # init method or constructor
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
        print("Year is", self.year)


toyota = car("Toyota Corolla", "blue", 2009)
kia = car("Kia Cerato", "green", 2020)

toyota.show() # same output as car.show(toyota)
kia.show() # same output as car.show(kia)

