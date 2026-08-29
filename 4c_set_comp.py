# Step 1: List with duplicate numbers
numbers = [1, 2, 2, 3, 4, 4, 5]
# Step 2: Create set of unique squares
squares_set = {x**2 for x in numbers}
# Step 3: Display the set
print("Set of unique squares:", squares_set)
