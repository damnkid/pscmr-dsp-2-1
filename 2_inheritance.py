from abc import ABC, abstractmethod
import math


class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Triangle Class
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Quadrilateral Class (assuming rectangle for simplicity)
class Quadrilateral(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Pentagon Class (regular pentagon)
class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Formula for regular pentagon area
        return (1 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (self.side**2)

    def perimeter(self):
        return 5 * self.side


# Main program
def main():
    while True:
        print("\nChoose Polygon Type:")
        print("1. Triangle")
        print("2. Quadrilateral (Rectangle)")
        print("3. Regular Pentagon")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))
            poly = Triangle(a, b, c)
        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            poly = Quadrilateral(length, width)
        elif choice == "3":
            side = float(input("Enter side length: "))
            poly = Pentagon(side)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
            continue

        print(f"Area: {poly.area():.2f}")
        print(f"Perimeter: {poly.perimeter():.2f}")


if __name__ == "__main__":
    main()
