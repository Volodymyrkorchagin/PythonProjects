from flat import Flat
from airplane import Airplane
from complex import Complex
from circle import Circle


if __name__ == "__main__":
    print("\n=== FLAT ===")

    flat1 = Flat(50, 100000)
    flat2 = Flat(60, 120000)
    flat3 = Flat(50, 90000)

    print(flat1 == flat3)
    print(flat1 != flat2)
    print(flat1 < flat2)
    print(flat2 > flat1)


    print("\n=== AIRPLANE ===")

    plane1 = Airplane(100, 150, "Boeing")
    plane2 = Airplane(50, 200, "Airbus")

    print(plane1 == plane2)
    print(plane1 > plane2)

    plane1 += plane2
    print(plane1.passenger)

    plane1 -= plane2
    print(plane1.passenger)

    print("\n=== COMPLEX ===")

    c1 = Complex(2, 3)
    c2 = Complex(1, 4)

    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)

    print("\n=== CIRCLE ===")

    circle1 = Circle(5)
    circle2 = Circle(7)
    circle3 = Circle(5)

    print(circle1 == circle3)   # True
    print(circle1 != circle2)   # True
    print(circle1 < circle2)    # True
    print(circle2 > circle1)    # True

    circle1 += circle2
    print(circle1.radius)

    circle1 -= circle2
    print(circle1.radius)