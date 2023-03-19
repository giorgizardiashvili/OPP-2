print(f"shemotane text {input()}")
print("ubralo text")


def __add__(self, other):
    if self.bottom == other.bottom:
        n_top = self.bottom
        n_bottom = self.top + self.bottom
    else:
        n_top = self.top * other.bottom + other.bottom * self.bottom
        n_bottom = self.bottom * other.bottom
        return Fraction(n_top, n_bottom)