class Car:
    def __init__(self, color, model, makeYear, fuelType):
        self.color = color
        self.model = model
        self.makeYear = makeYear
        self.fuelType = fuelType

    def __str__(self):
        return f"მანქანის მოდელი - {self.model} ფერი - {self.color}  გამოშვების წელი - {self.makeYear} საწვავის ტიპი - {self.fuelType}"

    def sell(self):
        return f"{self.model} {self.makeYear}-გაიყიდა"

    def buy(self):
        return f"{self.model} {self.makeYear}-იყიდა"

    def rent(self):
        return f"{self.model} {self.makeYear}-იქირავა"

    def insurance(self):
        return f"{self.model} {self.makeYear}-დააზღვია"


car = Car("red", "BMW", 2012, "gas")
print(car)
print(car.sell())