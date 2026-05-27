class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imag = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imaginary**2
        if denom == 0:
            raise ZeroDivisionError

        real = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imag = (self.imaginary * other.real - self.real * other.imaginary) / denom

        return Complex(real, imag)