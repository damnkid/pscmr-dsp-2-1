# method overloading
class Calculator:
    def add(self, *args):
        return sum(args)


# Main Program
calc = Calculator()

# Calling the same method with different numbers of arguments
print("Sum of 2 and 3:-", calc.add(2, 3))
print("Sum of 2, 3 and 4:-", calc.add(2, 3, 4))
print("Sum of 5, 10, 15, and 20:-", calc.add(5, 10, 15, 20))
