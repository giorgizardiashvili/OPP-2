class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return f"{self.top}/{self.bottom}"

    def __add__(self, other):
        if self.bottom == other.bottom:
            n_bottom = self.bottom
            n_top = self.top + other.bottom
        else:
            n_top = self.top * other.bottom + self.bottom * other.bottom
            n_bottom = self.bottom * other.bottom
        return Fraction(n_top, n_bottom)

    def inverse(self):
        return f"{self.bottom}/{self.top}"


f1 = Fraction(2, 3)
f2 = Fraction(3, 3)
f3 = f1 + f2 + f1
print(f1 + f2)
print(f3)
print(f3.inverse())