class Dog:
    def __init__(self, breed, size, age, color):
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color

    def __str__(self):
        return f"ძაღლის ჯიშია-{self.breed} ზომა-{self.size} ასაკი-{self.age} წლის ფერი-{self.color}"

    def eat(self):
        return f"{self.breed} ჭამს"

    def sleep(self):
        return f"{self.breed} სძინავს"

    def sit(self):
        return f"{self.breed} ზის"

    def run(self):
        return f"{self.breed} დარბის"


dog = Dog("Mastiff", "large", 5, "dark like nigger")
print(dog)
