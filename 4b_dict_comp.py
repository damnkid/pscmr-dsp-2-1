# Program: Dictionary from String with ASCII values
text = "HELLO"
# Step 2: Create dictionary with characters and ASCII values
adict = {char: ord(char) for char in text}
# Step 3: Display the dictionary
print("Dictionary with characters and their ASCII codes:")
print(adict)
