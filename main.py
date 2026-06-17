import timeit
from itertools import chain

# Sample data representing e-commerce categories
electronics = ["Laptop", "Smartphone", "Tablet"]
books = ["Python 101", "Clean Code", "Algorithms"]
clothing = ["T-Shirt", "Jeans", "Jacket"]

print("--- Python List Merging Methods ---\n")

# Method 1: Using the '+' operator (Creates a new list)
# Best for: Small lists, readability, keeping original lists intact.
merged_plus = electronics + books + clothing
print(f"1. '+' Operator: {merged_plus}")

# Method 2: Using the 'extend()' method (In-place modification)
# Best for: Modifying an existing list without creating a new one (memory efficient).
merged_extend = electronics.copy()  # Copy to keep original intact for demo
merged_extend.extend(books)
merged_extend.extend(clothing)
print(f"2. 'extend()' Method: {merged_extend}")

# Method 3: Using Asterisk/Unpacking Operator '*' (Python 3.5+)
# Best for: Merging and adding new elements on the fly.
merged_unpack = [*electronics, *books, "Smartwatch", *clothing]
print(f"3. Unpacking Operator '*': {merged_unpack}")

# Method 4: Using 'itertools.chain' (Lazy evaluation)
# Best for: Very large datasets where memory efficiency is critical.
# It returns an iterator instead of building the entire list in memory immediately.
merged_chain = list(chain(electronics, books, clothing))
print(f"4. 'itertools.chain': {merged_chain}\n")


# --- Performance Comparison ---
print("--- Performance Comparison (10,000 iterations) ---")
list_a = list(range(1000))
list_b = list(range(1000))

# Benchmark '+'
time_plus = timeit.timeit("list_a + list_b", globals=globals(), number=10000)
print(f"'+' Operator time:      {time_plus:.4f} seconds")

# Benchmark 'extend'
time_extend = timeit.timeit(
    "temp = list_a.copy(); temp.extend(list_b)", globals=globals(), number=10000
)
print(f"'extend()' Method time:  {time_extend:.4f} seconds (includes copy)")

# Benchmark Unpacking
time_unpack = timeit.timeit("[*list_a, *list_b]", globals=globals(), number=10000)
print(f"Unpacking '*' time:     {time_unpack:.4f} seconds")

# Benchmark itertools.chain
time_chain = timeit.timeit("list(chain(list_a, list_b))", globals=globals(), number=10000)
print(f"'itertools.chain' time: {time_chain:.4f} seconds")
