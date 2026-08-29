# Class Definition
class Flower:
    def __init__(self, name, num_petals, price):
        self.name = name
        self.num_petals = num_petals
        self.price = price

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_num_petals(self, num_petals):
        self.num_petals = num_petals

    def set_price(self, price):
        self.price = price

    # Getter methods
    def get_name(self):
        return self.name

    def get_num_petals(self):
        return self.num_petals

    def get_price(self):
        return self.price


# Main Program
flower1 = Flower("Rose", 32, 10.5)

# Display initial values
print("Flower Name:", flower1.get_name())
print("Number of Petals:", flower1.get_num_petals())
print("Price:", flower1.get_price())

# Update values
flower1.set_name("Lily")
flower1.set_num_petals(6)
flower1.set_price(15.75)

# Display updated values
print("\nAfter updating:")
print("Flower Name:", flower1.get_name())
print("Number of Petals:", flower1.get_num_petals())
print("Price:", flower1.get_price())
