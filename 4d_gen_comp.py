# 1) Basic: squares of 1..10 (generator)
squares_gen = (n * n for n in range(1, 11))
print("Type of squares_gen:", type(squares_gen))

# Consume with next()
print("First two values via next():", next(squares_gen), next(squares_gen))

# Continue consumption with a loop (picks up where next() left off)
print("Remaining squares:", list(squares_gen))  # list() just to display what's left

# 2) Filter + transform: even squares up to 20
even_squares = (n * n for n in range(1, 21) if n % 2 == 0)
print("Even squares up to 20:", list(even_squares))

# 3) Aggregate directly on generator (no intermediate list)
cubes_sum = sum(n**3 for n in range(1, 6))  # 1^3 + ... + 5^3
print("Sum of cubes 1..5:", cubes_sum)

# 4) any/all with conditions
has_multiple_of_7 = any(n % 7 == 0 for n in range(10, 20))
all_small = all(n < 50 for n in range(10, 20))
print("Any multiple of 7 in 10..19?:", has_multiple_of_7)
print("Are all numbers < 50 in 10..19?:", all_small)

# 5) Working with strings: word lengths lazily
sentence = "Generator expressions are memory efficient and fast"
word_lengths = (len(w) for w in sentence.split())
print("Word lengths:", list(word_lengths))

list_comp = [n * n for n in range(1, 11)]
gen_comp = (n * n for n in range(1, 11))
print("List comp (materialized):", list_comp)
print("Gen comp (lazy, not materialized):", gen_comp)  # shows generator object
print("Materialize generator on demand:", list(gen_comp))
