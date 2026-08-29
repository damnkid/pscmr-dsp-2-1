# Program: Generate Combinations of n Distinct Objects
from itertools import combinations

# Step 1: Define the original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 2: Define the size of each combination (r)
r = 2

# Step 3: Generate combinations
comb = combinations(original_list, r)

# Step 4: Print combinations
print("Original List:", original_list)
print(f"Combinations of {r} distinct objects:")
for c in comb:
    print(list(c))
